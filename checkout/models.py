from django.db import models
from category.models import Category
from product.models import Products
from accounts.models import Customer


class Check(models.Model):
    product=models.ForeignKey(Products, on_delete=models.CASCADE, null=True,blank=True)
    Custometr=models.ForeignKey(Customer, on_delete=models.CASCADE, null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True,blank=True)
    status=models.IntegerField(default=0,blank=True,null=True)

    def __str__(self):
        return self.product.name