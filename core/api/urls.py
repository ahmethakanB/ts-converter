from rest_framework.routers import DefaultRouter
from core.api.views import OrderDetailViewSet

router = DefaultRouter()
router.register(r'order-details', OrderDetailViewSet, basename='order-details')
urlpatterns = router.urls