from rest_framework import (
    viewsets,
    filters,
)
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView, DestroyAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core.api.serializers import OrderDetailSerializer, ProductSerializer, OrderSerializer
from core.models import Product, Order, OrderType
from core.utils.filters.odata_backend import ODataFilterBackend


class OrderDetailViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer

    filter_backends = (
        ODataFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    )

    ordering_fields = ("name", "start_datetime", "type__name")
    search_fields = ("name", "description", "type__name", "products__name")

    def get_queryset(self):
        return Order.objects.select_related("type").prefetch_related("products")


class ProductAPI(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class   = ProductSerializer
    queryset           = Product.objects.all()
    filter_backends    = (
        ODataFilterBackend,
        OrderingFilter,
        SearchFilter,
    )

class OrderTypeAPI(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class   = ProductSerializer
    queryset           = OrderType.objects.all()
    filter_backends    = (
        ODataFilterBackend,
        OrderingFilter,
        SearchFilter,
    )

class DeleteOrderAPI(DestroyAPIView):
    permission_classes = (AllowAny,)
    serializer_class   = OrderSerializer
    queryset           = Order.objects.all()
    filter_backends    = (
        ODataFilterBackend,
        OrderingFilter,
        SearchFilter,
    )

class CreateOrderAPI(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = OrderSerializer
    queryset = Order.objects.all()