from django.db import models
from django.db.models.query_utils import select_related_descend

# Create your models here.
class Producto(models.Model):
  nombre = models.CharField(max_length=40)
  categoria = models.CharField(max_length=30)
  precio = models.IntegerField(default=0)

#definimos la salida
  def __str__(self):
      return f'{self.nombre} , {self.categoria} , {self.precio}'