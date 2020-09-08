from django.db import models
from content import generate
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator,MinValueValidator,MaxLengthValidator,RegexValidator
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    user_type = models.CharField(max_length=20, null=False, blank=False)
    phone = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')],null=True, blank=True)
    address = models.CharField(max_length=255,null=True, blank=True)
    city = models.CharField(max_length=50,null=True, blank=True)
    state = models.CharField(max_length=50,null=True, blank=True)
    country = models.CharField(max_length=50,null=True, blank=True)
    pincode = models.CharField(max_length=6, validators=[RegexValidator(r'^\d{1,10}$')],null=True, blank=True)
    
    USERNAME_FIELD = 'user__email'
    REQUIRED_FIELDS = ['user__first_name', 'user__last_name','phone', 'pincode']

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return "{0} - {1}".format(self.user.username, self.user_type)

    

class AuthorManager(models.Model):
    def get_queryset(self):
        return super().get_queryset().filter(profile__user_type="Author")

class Author(User):
    class Meta:
        ordering = ("username",)
        proxy = True
    
    objects = AuthorManager()
    
    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])
    
    @receiver(post_save, sender=User)
    def user_is_created(sender, instance, created, **kwargs):
        print(created)
        if created:
            Profile.objects.create(user=instance)
        else:
            instance.profile.save()
    
    from django.contrib.auth.models import User

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)
    User.add_to_class('full_name', full_name)

    

