import factory
from account.models import User, UserProfile

class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    first_name = 'Test'
    last_name = 'User'
    username = 'testuser'
    email = 'test.user@example.com'
    password = factory.PostGenerationMethodCall('set_password', 'password')


class UserProfileFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = UserProfile

    user = factory.SubFactory(UserFactory, username=factory.Faker('email'))
    phone = '9876543210'
    address = 'test street'
    address = '37 Baker Street'
    pincode = '342004'
    

class AdminFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    first_name = 'Test'
    last_name = 'User'
    username = 'testuser'
    email = 'test.user@example.com'
    password = factory.PostGenerationMethodCall('set_password', 'password')
    is_superuser = True
    is_staff = True


