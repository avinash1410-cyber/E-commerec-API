from django.db import models
from category.models import Category
from artist.models import Artist



class Products(models.Model):
    Offer = (
        ("first", "10"),
        ("second", "15"),
        ("third", "20"),
        ("fourth", "22"),
        ("fifth", "25"),
    )

    name = models.CharField(max_length=60)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(default='default.jpg', upload_to='product',null=True)
    artist=models.ForeignKey(Artist, on_delete=models.CASCADE, null=True,blank=True)
    created=models.DateField(auto_now_add=True)
    offer= models.CharField(max_length=20,default="10",choices = Offer, null=True)



    @property
    def get_all_products(self):
        return Products.objects.all()

    # @staticmethod
    # def get_all_products_by_categoryid(category_id):
    #     if category_id:
    #         return Products.objects.filter(category=category_id)
    #     else:
    #         return Products.get_all_products()

    @property
    def disc_price(self):
        return self.price*self.category.disc

    def __str__(self):
        return self.name