from django.shortcuts import render
from rest_framework import generics, filters, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from account.permissions import IsLoggedInUserOrAdmin, IsAdminUser
from account.models import User
from .serializers import UserSerializer
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name', 'user__username', 'user__email')
    ordering_fields = '__all__'
    ordering = ('-id',)
    
    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]