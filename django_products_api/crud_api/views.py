from ast import expr_context
from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from .serializers import ProductSerializer
from rest_framework.views import APIView
from .models import Product
from rest_framework.response import Response

# Create views
class ListProductAPIView(ListAPIView):
  # Endpoint to list all of the available products from the database
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

class DetailProductAPIView(RetrieveAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer


class CreateProductAPIView(CreateAPIView):
  # Endpoint allows the creation of new products
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

class UpdateProductAPIView(UpdateAPIView):
  # Endpoint allows updating a specific product by passing in the id of the product
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

class DeleteProductAPIView(DestroyAPIView):
  # Endpoint allows to delete a specific product from the database
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
