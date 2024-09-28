from rest_framework.serializers import ModelSerializer #type: ignore
from . import models #type: ignore

class ProductTypeSerializer(ModelSerializer):
    class Meta:
        model = models.ProductType
        feilds = "__all__"

class ProductSerializer(ModelSerializer):
    class Meta:
        model = models.Product
        fields = "__all__"