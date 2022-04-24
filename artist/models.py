from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from accounts.models import Customer


class Artist(models.Model):
    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50,null=True)
    # phone = models.CharField(max_length=10)
    # email = models.EmailField(null=True)
    # password = models.CharField(max_length=100,null=True)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')