from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProductViewSet, CategoryViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('products', ProductViewSet)
router.register('category', CategoryViewSet)

urlpatterns = [] + router.urls
