from rest_framework import serializers
from .models import Products

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        ordering = ['-created']
        fields='__all__'