from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class meta:
        model = Product
        fields = "__all__"
