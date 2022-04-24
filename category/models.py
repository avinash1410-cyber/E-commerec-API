from django.db import models

# Create your models here.

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    disc=models.FloatField(null=True,default=1)
    slug = models.SlugField(max_length = 255,null=True,blank=True)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    def __str__(self):
        return self.name