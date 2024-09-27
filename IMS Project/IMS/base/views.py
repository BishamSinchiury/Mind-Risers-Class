from django.shortcuts import render #type: ignore
from . import models  #type: ignore
from rest_framework.viewsets import ModelViewSet #type: ignore
from . import serializers
# Create  your views here.

class ProductTypeApiView(ModelViewSet):
    queryset = models.ProductType.objects.all()
    serializer_class =  serializers.ProductTypeSerializer
