from django.db import models
from django.db.models.query_utils import select_related_descend

# Create your models here.
class Product(models.Model):
  name = models.CharField(max_length=40)
  category = models.CharField(max_length=30)
  price = models.IntegerField(default=0)

#definimos la salida
  def __str__(self):
      return f'{self.name} , {self.category} , {self.price}'