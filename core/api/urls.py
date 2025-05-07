from django.urls import (
    path,
)

from rest_framework.routers import DefaultRouter
from core.api.views import OrderDetailViewSet, ProductAPI, OrderTypeAPI, DeleteOrderAPI, CreateOrderAPI

router = DefaultRouter()
urlpatterns = [
    path('get-product/', ProductAPI.as_view(), name="get-product"),
    path('get-order-type/', OrderTypeAPI.as_view(), name="get-order-type"),
    path('delete-order/', DeleteOrderAPI.as_view(), name="delete-order"),
    path('create-order/', CreateOrderAPI.as_view(), name="create-order"),
]
router.register(r'order-details', OrderDetailViewSet, basename='order-details')
urlpatterns += router.urls