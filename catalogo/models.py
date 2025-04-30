from django.db import models


# Create your models here.
class Jerarquia(models.Model):
    nombre = models.CharField(null=False, unique=True, max_length=255)

    def __str__(self):
        return f"{self.pk} {self.nombre}"


class Tipo(models.Model):
    nombre = models.CharField(null=False, unique=True, max_length=255)

    def __str__(self):
        return f"{self.pk} {self.nombre}"


class Cuenta(models.Model):
    nombre = models.CharField(unique=True, null=False, max_length=255)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    jerarquia = models.ForeignKey(Jerarquia, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True, null=False)

    def __str__(self):
        return f"{self.nombre}"