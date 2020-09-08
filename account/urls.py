from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import AuthorViewSet,LoginView,LogoutView

router = routers.DefaultRouter()
router.register('users',AuthorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/login/', LoginView.as_view()),
    path('auth/logout/', LogoutView.as_view()),
    # path('rest-auth/registration/', include('rest_auth.registration.urls'))
    
]