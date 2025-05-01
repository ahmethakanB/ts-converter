from rest_framework import serializers

from core.models import Product, Order
from core.utils.api import DynamicFieldsModelSerializer


class OrderDetailSerializer(DynamicFieldsModelSerializer):
    order_type = serializers.CharField(source="type.name", read_only=True)
    products = serializers.PrimaryKeyRelatedField(
        queryset=Order.products.rel.model.objects.all(),
        many=True
    )

    #TODO Burada Fazlalık İse Kaldır
    def __init__(self, *args, **kwargs):
        request = kwargs.get('context', {}).get('request')
        if request is not None and hasattr(request, '_odata_select'):
            kwargs['fields'] = request._odata_select
        super().__init__(*args, **kwargs)

    class Meta:
        model  = Order
        fields = (
            'id',
            'name',
            'products',
            'type',
            'start_datetime',
            'end_datetime',
            'order_type',
        )

    def create(self, validated_data):
        products = validated_data.pop("products", [])
        order = Order.objects.create(**validated_data)
        order.products.set(products)
        return order

    def update(self, instance, validated_data):
        products = validated_data.pop("products", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if products is not None:
            instance.products.set(products)
        return instance
