from rest_framework import serializers
# from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator
from rest_framework.response import Response
from account.models import User,UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserProfile
        fields = ('phone','address','city','state','country','pincode')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer(required=True)
    full_name = serializers.SerializerMethodField()
    

    def get_full_name(self,obj):
        try:
            return obj.first_name + ' ' + obj.last_name  
        except:
            None
    
    class Meta:
        model = User
        fields = ('url', 'email', 'full_name', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True,'required':True}}
    
    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user, **profile_data)
        return user
    
    
    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.phone = profile_data.get('phone', profile.phone)
        profile.address = profile_data.get('address', profile.address)
        profile.country = profile_data.get('country', profile.country)
        profile.city = profile_data.get('city', profile.city)
        profile.pincode = profile_data.get('pincode', profile.pincode)
        profile.save()

        return instance
    