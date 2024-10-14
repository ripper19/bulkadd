from rest_framework import serializers
from .models import Product, Variant

class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = ['variant_name', 'sku', 'price', 'details']
    
class ProductSerializer(serializers.ModelSerializer):
    variants = VariantSerializer(many = True)
    
    class Meta:
        model = Product
        fields = ['name', 'image','variants']
        