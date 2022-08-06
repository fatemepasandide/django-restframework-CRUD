from distutils.command.upload import upload
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    #image = models.ImageField(upload_to=)

    def __str__(self):
        return self.name


