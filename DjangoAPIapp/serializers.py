from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','title']
    
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'
