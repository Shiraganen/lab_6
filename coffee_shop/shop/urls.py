from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, CoffeeViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'coffees', CoffeeViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = router.urls
