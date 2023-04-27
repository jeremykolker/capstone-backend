from django.db import models

# Create your models here.
class Item(models.Model):
    photo = models.URLField(null=True, blank=True)
    name = models.CharField(max_length=32)
    color = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=20)
    description = models.TextField()
