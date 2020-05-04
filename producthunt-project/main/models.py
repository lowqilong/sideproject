from django.db import models
from datetime import datetime

# Create your models here.    

class 

class Categories(models.Model):
    category = models.CharField(max_length=200)

    slug = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category

class Sales(models.Model):
    category = models.ForeignKey(Categories, default=1, verbose_name="category", on_delete=models.SET_DEFAULT)
    discount = models.IntegerField()
    # image = models.ImageField(upload_to='static/uploads/', height_field=None, width_field=None, max_length=100)
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.category.category

class Tags(models.Model):
    tag = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.tag

class Products(models.Model):
    name = models.CharField(max_length=200)
    published = models.DateTimeField("date published", default=datetime.now())
    # image = models.ImageField(upload_to='static/uploads/', height_field=None, width_field=None, max_length=100)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.IntegerField()
    category = models.ForeignKey(Categories, default=1, verbose_name="category", on_delete=models.SET_DEFAULT)

    @property
    def discount(self):
        if Sales.objects.get(category = self.category):
            return Sales.objects.get(category = self.category).select_related('discount')
        else:
            return 0


    def __str__(self):
        return self.name


    

