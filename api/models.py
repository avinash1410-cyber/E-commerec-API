from django.db import models


class Order(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    owner=models.CharField(max_length=20,null=True,blank=True)
    def __str__(self):
         return self.name