from rest_framework import serializers
from .models import Content, Category
# from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator
from rest_framework.response import Response

class ContentListSerializer(serializers.ModelSerializer):


    class Meta:
        model = Content
        fields = ('id','title')

class ContentSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    def get_category(self, obj):
        return obj.category.name
    class Meta:
        model = Content
        fields = ('id','title','body','summary','category')

class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name',)
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'