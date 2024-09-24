from rest_framework.serializers import ModelSerializer #type: ignore
from . import models

class ProductTypeSerializer(ModelSerializer):
    class Meta:
        model = models.ProductType
        fields = "__all__"
