from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
from django.db import models
from django.contrib.auth.models import User
class Customer(models.Model):
    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50,null=True)
    # phone = models.CharField(max_length=10)
    # email = models.EmailField(null=True)
    # password = models.CharField(max_length=100,null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return str(self.user)
    @property
    def name(self):
        return self.__str__()