from django.db import models

class DiscountManager(models.Manager):
    def have_discount(self, sales):
        if 

class PostQuerySet(models.QuerySet):
    