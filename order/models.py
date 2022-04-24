from django.db import models
import datetime

from accounts.models import Customer
from product.models import Products


class Order(models.Model):
	STATUS = (
		("Book", "Book"),
		("Dis", "Dispatch"),
		("Del", "Delivered"),
	)

	product = models.ForeignKey(Products,on_delete=models.CASCADE,null=True,blank=True)
	customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,blank=True)
	quantity = models.IntegerField(default=1)
	address = models.CharField(max_length=50, default='', blank=True,null=True)
	date = models.DateField(default=datetime.datetime.today)
	status = models.CharField(max_length=20,default="Add to cart",choices = STATUS, null=True)

	# def placeOrder(self):
	# 	self.save()

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

	@staticmethod
	def get_orders_by_customer(customer_id):
		Cust=Customer.objects.get(id=customer_id)
		return Order.objects.filter(customer=Cust).order_by('-date')

	def __str__(self):
		oreder=self.product.name,"to",self.customer.name
		return str(oreder)