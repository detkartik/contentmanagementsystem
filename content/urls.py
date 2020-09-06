from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import ContentViewSet,CategoryViewSet

router = routers.DefaultRouter()
router.register('content',ContentViewSet)
router.register('category',CategoryViewSet)
urlpatterns = [
    path('', include(router.urls)),
    
]