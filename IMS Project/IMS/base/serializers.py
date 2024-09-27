from rest_framework.serializers import ModelSerializer #type: ignore
from . import models #type: ignore

class ProductTypeSerializer(ModelSerializer):
    class Meta:
        model = models.ProductType
        feilds = "__all__"

