from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Product

User = get_user_model()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'place', 'price')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    order = ProductSerializer(many=True, read_only=False, required=False)

    def update(self, instance, validated_data):
        order_data = validated_data.pop('order')
        order = instance.order
        for product_data in order_data:
            product_data = list(product_data.items())
            product = product_data.pop(0)
            try:
                prod = Product.objects.get(name=product[1])
                order.add(prod)
            except Product.DoesNotExist:
                order.clear()

        return instance

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'phone', 'order')
