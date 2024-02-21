from django.shortcuts import render,get_object_or_404
from .models import Category,Product,Orders,Title
from .serializers import CategorySerializer,ProductSerializer,OrdersSerializer,TitleSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

 
@api_view(['POST'])
def add_products(request):
    serializer = ProductSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_detail(request,pk):
    products = get_object_or_404(Product,pk=pk)
    serializer = ProductSerializer(products, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def update_products(request,pk):
    product = Product.objects.get(pk=pk)
    serializer = ProductSerializer(instance=product, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_products(request,pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)





@api_view(['POST'])
def add_category(request):
    serializer = CategorySerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_category(request):
    products = Category.objects.all()
    serializer = CategorySerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_detail_category(request,pk):
    products = get_object_or_404(Category,pk=pk)
    serializer = CategorySerializer(products, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def update_category(request,pk):
    product = Category.objects.get(pk=pk)
    serializer = CategorySerializer(instance=product, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_category(request,pk):
    product = get_object_or_404(Category, pk=pk)
    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)