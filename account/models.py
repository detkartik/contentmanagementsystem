from django.db import models
from content import generate
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator,MinValueValidator,MaxLengthValidator,RegexValidator
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    is_admin = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')],null=True, blank=True)
    address = models.CharField(max_length=255,null=True, blank=True)
    city = models.CharField(max_length=50,null=True, blank=True)
    state = models.CharField(max_length=50,null=True, blank=True)
    country = models.CharField(max_length=50,null=True, blank=True)
    pincode = models.CharField(max_length=6, validators=[RegexValidator(r'^\d{1,10}$')],null=True, blank=True)
    
    REQUIRED_FIELDS = ['phone', 'pincode']

    def __unicode__(self):
        return self.user.email

    def get_full_name(self):
        return ' '.join([self.user.first_name, self.user.last_name])


    


    

