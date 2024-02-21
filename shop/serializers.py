from rest_framework import serializers
from . models import Product,Category,Orders,Title

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'
        
class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = '__all__'
        
class OrdersSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Orders
        fields = '__all__'
        
class TitleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Title
        fields = '__all__'