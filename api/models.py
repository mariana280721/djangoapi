from django.db import models

class Producto(models.Model):
    codigo= models.CharField(max_length=200)
    nombre= models.CharField(max_length=200)
    descripcion= models.CharField(max_length=500)
    precio= models.FloatField()

    def __str__(self):
        return self.codigo

