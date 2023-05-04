from django.db import models

# Create your models here.
class Raza(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombreRaza = models.CharField(max_length=20, verbose_name='Nombre d ela Raza')

    def __str__(self):
        return self.nombreRaza

class Mascota(models.Model):
    codigoChip = models.IntegerField(primary_key=True, verbose_name='Chip de la Mascota')
    nombreMascota = models.CharField(max_length=30, verbose_name='Nombre de la Mascota')
    edadMascota = models.IntegerField(verbose_name='Edad de la mascota')
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreMascota


