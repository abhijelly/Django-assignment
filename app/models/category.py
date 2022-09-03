from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    """
    OS = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    price = models.IntegerField()
    
    """

    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    
    def __str__(self):
        return self.name