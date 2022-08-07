from rest_framework import serializers
from .models import Product

class ProductSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'price',
            'description',
            'quantity',
        ]