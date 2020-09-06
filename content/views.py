from django.shortcuts import render
from rest_framework import generics, filters, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from account.permissions import IsLoggedInUserOrAdmin, IsAdminUser
from .models import Content, Category
from .serializers import ContentSerializer, CategorySerializer
# Create your views here.
class ContentViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,IsAdminUser,IsLoggedInUserOrAdmin)
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    

class CategoryViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,IsAdminUser,IsLoggedInUserOrAdmin)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    