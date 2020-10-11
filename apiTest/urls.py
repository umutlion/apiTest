from .views import PostViewSet, CategoryViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('posts', PostViewSet, basename='post')
router.register('categories', CategoryViewSet, basename='category')

urlpatterns = router.urls
