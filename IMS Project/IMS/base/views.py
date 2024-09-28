from django.shortcuts import render #type: ignore
from . import models  #type: ignore
from rest_framework.viewsets import ModelViewSet #type: ignore
from . import serializers
from rest_framework.generics  import GenericAPIView #type: ignore
from rest_framework.response import Response #type: ignore


# Create  your views here.

class ProductTypeApiView(ModelViewSet):
    queryset = models.ProductType.objects.all()
    serializer_class =  serializers.ProductTypeSerializer

class ProductApiView(GenericAPIView):

    def get(self, request):
        project_objs = models.Product.objects.all()
        serializer = serializers.ProductSerializer(project_objs, many=True)
        return Response(serializer)
    
    def post(self, resquest):
        serializer = serializers.ProductSerializer(data=resquest.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Data Created')
        else:
            return Response(serializer.errors)
        
class ProductDetailApiView(GenericAPIView):
    def get(self, request, pk):
        product_obj = models.Product.objects.get(pk=pk)
        serializer = serializers.ProductSerializer(product_obj)
        return Response(serializer.data)


