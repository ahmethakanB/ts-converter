from rest_framework import (
    viewsets,
    filters,
)
from rest_framework.permissions import IsAuthenticated, AllowAny

from core.api.serializers import OrderDetailSerializer
from core.models import Product, Order
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
