from django.db import models
from category.models import Category



class Products(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(default='default.jpg', upload_to='product',null=True)

    def __str__(self):
        return self.name

    # @staticmethod
    @property
    def get_products_by_id(ids):
        return Products.objects.filter(id__in=ids)

    @property
    def get_all_products(self):
        return Products.objects.all()

    @property
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Products.objects.filter(category=category_id)
        else:
            return Products.get_all_products()

    @property
    def disc_price(self):
        return self.price*self.category.disc

    def __str__(self):
        return self.name