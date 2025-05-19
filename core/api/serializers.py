from rest_framework import serializers

from core.models import Product, Order, OrderType
from core.utils.api import DynamicFieldsModelSerializer


class OrderDetailSerializer(DynamicFieldsModelSerializer):
    products = serializers.PrimaryKeyRelatedField(
        queryset=Order.products.rel.model.objects.all(),
        many=True
    )

    # TODO Burada Fazlalık İse Kaldır
    def __init__(self, *args, **kwargs):
        request = kwargs.get('context', {}).get('request')
        if request is not None and hasattr(request, '_odata_select'):
            kwargs['fields'] = request._odata_select
        super().__init__(*args, **kwargs)

    class Meta:
        model = Order
        fields = (
            'id',
            'name',
            'products',
            'type',
            'start_datetime',
            'end_datetime',
        )


class ProductSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'price',
            'stock',
            'is_dismantling',
            'is_plannable',
        )


class OrderTypeSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = OrderType
        fields = (
            'id',
            'name',
        )


class CreateOrder(DynamicFieldsModelSerializer):
    """CreateAPIView için kullanılır."""
    products = serializers.PrimaryKeyRelatedField(
        queryset=Order.products.rel.model.objects.all(),
        many=True
    )

    class Meta:
        model = Order
        fields = (
            'name',
            'products',
            'type',
            'start_datetime',
            'end_datetime',
        )

    def create(self, validated_data):
        products = validated_data.pop("products", [])
        order = Order.objects.create(**validated_data)
        order.products.set(products)
        return order


class UpdateOrder(DynamicFieldsModelSerializer):
    """UpdateAPIView için kullanılır."""
    products = serializers.PrimaryKeyRelatedField(
        queryset=Order.products.rel.model.objects.all(),
        many=True,
        required=False,
    )

    class Meta:
        model = Order
        fields = (
            'name',
            'products',
            'type',
            'start_datetime',
            'end_datetime',
        )

    def update(self, instance, validated_data):
        products = validated_data.pop("products", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if products is not None:
            instance.products.set(products)
        return instance


class DeleteOrder(serializers.Serializer):
    """DestroyAPIView için, genellikle payload almaz."""
    pass
