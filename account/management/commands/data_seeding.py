import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','contentmanagementsystem.settings')
import random
import datetime
# from account.models import UserProfile
from django.core.management import BaseCommand
from account.models import *


""" Clear all data and creates addresses """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'

class Command(BaseCommand):
    help = "seed database to admin for testing and development."

    first_names = ('John','Andy','Joe')
    last_names = ('Johnson','Smith','Williams')
    phone = ('9876543210','9999999999','7890123456')
    address = ('37 Baker Street','308 WDC','XX4 Dueoi')
    pincode = ('342004','560024','560003')
    code = ('IN','US','NZ')

    def create_random_user(self, count):
        data = {
            'username' : random.choice(self.first_names) + str(count),
            'password' : 'user' + str(count),
            'first_name' : random.choice(self.first_names),
            'last_name' : random.choice(self.last_names),
            'phone': random.choice(self.phone),
            'address':random.choice(self.address),
            'pincode':random.choice(self.pincode),
            'country' : random.choice(self.code),
        }
        return User.objects.create_user(**data)

    def handle(self, *args, **kwargs):
        print('Creating dummy data')
        user = User.objects.get(username='admin')
        for count in range(1,251):
            data = {
                'user' : user
            }
            Profile.objects.create(**data)
            if count % 10 == 0:
                user = self.create_random_user(count)
        print('Creation of dummy data is completed')