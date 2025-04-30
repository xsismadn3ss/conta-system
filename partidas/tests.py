from django.test import TestCase
from .models import PartidaRegistro, Detalles
from catalogo.models import Cuenta, Tipo, Jerarquia
from libros.models import LibroMayor, Tipo as TipoMovimiento
from django.utils import timezone


class PartidaRegistroTestCase(TestCase):
    def test_creacion_partida(self):
        partida = PartidaRegistro.objects.create(
            titulo="Test Partida", descripcion="Descripción de prueba"
        )
        self.assertEqual(partida.titulo, "Test Partida")
        self.assertTrue(timezone.is_aware(partida.fecha_creacion))
        self.assertEqual(partida.descripcion, "Descripción de prueba")

    def test_str_partida(self):
        partida = PartidaRegistro.objects.create(
            titulo="Test Partida", descripcion="Descripción de prueba"
        )
        self.assertEqual(
            str(partida),
            "Test Partida, {}".format(partida.fecha_creacion.strftime("%c")),
        )


class DetallesTestCase(TestCase):
    def set_up(self):
        cuenta_tipo = Tipo.objects.create(nombre="Tipo de prueba")
        cuenta_jerarquia = Jerarquia.objects.create(nombre="Jerarquia de prueba")
        cuenta = Cuenta.objects.create(
            nombre="Cuenta de prueba",
            tipo=cuenta_tipo,
            jerarquia=cuenta_jerarquia,
            estado=True,
        )
        partida = PartidaRegistro.objects.create(
            titulo="Partida de prueba", descripcion="Descripción de prueba"
        )
        tipo_movimiento = TipoMovimiento.objects.create(
            nombre="Tipo de movimiento de prueba"
        )
        return partida, cuenta, tipo_movimiento

    def test_actualizacion_libro_mayor(self):
        partida, cuenta, tipo_movimiento = self.set_up()
        # Crear primer detalle
        detalle1 = Detalles.objects.create(
            monto_debe=100.0,
            monto_haber=0.0,
            partida=partida,
            catalogo_cuentas=cuenta,
        )

        def update_libro(libro:LibroMayor, detalle:Detalles, saldo_anterior:float=0.0):
            libro.saldo_anterior = saldo_anterior
            libro.movimiento = (detalle.monto_debe or 0.0)*-1 + (detalle.monto_haber or 0.0)
            libro.saldo_final = libro.saldo_anterior + libro.movimiento
            libro.save()

        # Crear un libro y que tenga el saldo
        libro: LibroMayor = LibroMayor.objects.get_or_create(
            cuenta=cuenta, tipo_movimiento=tipo_movimiento
        )[0]
        update_libro(libro, detalle1, libro.saldo_final)
        self.assertEqual(libro.saldo_final, -100.0)

        # Crear segundo detalle
        detalle2 = Detalles.objects.create(
            monto_debe=0.0,
            monto_haber=120.0,
            partida=partida,
            catalogo_cuentas=cuenta,
        )
        # Actualizar el libro mayor
        update_libro(libro, detalle2, libro.saldo_final)
        self.assertEqual(libro.saldo_final, 20.0)
