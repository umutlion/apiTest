from django.contrib import admin
from django.urls import path, include
from .views import post_list, post_detail, PostAPIView, PostDetails, GenericAPIView, PostViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('post', PostViewSet, basename='post')

urlpatterns = [
    #path('post/', post_list),
    path('post/', PostAPIView.as_view()),
    #path('post/<int:pk>/', post_detail),
    path('detail/<int:id>/', PostDetails.as_view()),
    path('generic/post/<int:id>/', GenericAPIView.as_view()),
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),

]
