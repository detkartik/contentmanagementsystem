from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import ContentViewSet,CategoryViewSet,UserViewSet

router = routers.DefaultRouter()
router.register('users',UserViewSet)
router.register('content',ContentViewSet)
router.register('category',CategoryViewSet)
urlpatterns = [
    path('', include(router.urls)),
    
]