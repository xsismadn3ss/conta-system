from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Tipo(models.Model):
    nombre = models.CharField(unique=True, null=False, max_length=50)

    def __str__(self):
        return f"nombre: {self.nombre}"


class LibroMayor(models.Model):
    saldo_anterior = models.FloatField()
    movimiento = models.FloatField()
    saldo_final = models.FloatField(editable=False)  # No editable manualmente
    
    tipo_movimiento = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    cuenta = models.ForeignKey("catalogo.Cuenta", on_delete=models.CASCADE, default=None, null=True)

    def save(self, *args, **kwargs):
        # Calcula el saldo final automáticamente
        self.saldo_final = self.saldo_anterior + self.movimiento
        super().save(*args, **kwargs)

    def __str__(self):
        return "saldo anterior: {}, movimiento: {}, saldo final: {}".format(
            self.saldo_anterior, self.movimiento, self.saldo_final
        )
