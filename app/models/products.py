from django.db import models
from .category import Category

class Products(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    @staticmethod
    def get_all_products():
        return Products.objects.all()

    def __str__(self):
        return self.name