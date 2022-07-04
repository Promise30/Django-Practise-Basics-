from django.db import models
from datetime import datetime
# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=20, default="Unknown name")
    price = models.DecimalField(max_digits=100, decimal_places=2)
    description = models.TextField()
    year_guarantee = models.PositiveSmallIntegerField()
    availability = models.BooleanField()
    published = models.DateField(default=datetime.now)

    def __str__(self):
        return f'Product Name: {self.product_name}, Price: {self.price}, Description: {self.description}'