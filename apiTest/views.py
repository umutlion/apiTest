from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer

from rest_framework.viewsets import ModelViewSet

# Create your views here.


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # http_method_names = ['get', 'put', 'head']


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
