from django.contrib import admin
from .models import Sales, Products, Categories, Tags
from django.db import models

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Name/date", {"fields": ["name", "published"]}),
        ("Image", {"fields": ["image"]}),
        ("Description", {"fields": ["description"]}),
        ("Price", {"fields": ["price"]}),
        ("Quantity", {"fields": ["quantity"]}),
        ("Category", {"fields": ["category"]})
    ]

admin.site.register(Categories)
admin.site.register(Tags)
admin.site.register(Sales)
admin.site.register(Products, ProductAdmin)

