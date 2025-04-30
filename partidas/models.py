from django.db import models
from django.utils import timezone


# Create your models here.
class PartidaRegistro(models.Model):
    titulo = models.CharField(max_length=100, null=False)
    fecha_creacion = models.DateTimeField(default=timezone.now, null=False)  # Cambiado a timezone.now
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.titulo}, {self.fecha_creacion:%c}"


class Detalles(models.Model):
    monto_debe = models.FloatField(null=True)
    monto_haber = models.FloatField(null=True)

    partida = models.ForeignKey(PartidaRegistro, on_delete=models.CASCADE)
    catalogo_cuentas = models.ForeignKey("catalogo.Cuenta", on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"monto debe: {self.monto_debe}, monto_haber: {self.monto_haber}"
    