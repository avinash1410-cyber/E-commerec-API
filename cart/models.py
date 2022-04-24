from django.db import models
from category.models import Category
from product.models import Products
from accounts.models import Customer
from order.models import Order

class Cart(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE, null=True,blank=True)
    Customer =models.ForeignKey(Customer, on_delete=models.CASCADE, null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True,blank=True)

    @property
    def get_cart_total(self):
        orderitems = self.order_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_quantity(self):
        quauntity = self.order.quantity
        return quauntity