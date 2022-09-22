from pyexpat import model
from django.db import models

class Product(models.Model):
  product_name = models.CharField(max_length=50)
  price = models.FloatField(default=0)
  product_image = models.ImageField(default=None)
  manufacturer = models.CharField(max_length=100)
  date_listed = models.DateField(auto_now_add=True)

  def __str__(self):
    return self.product_name

