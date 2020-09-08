
from django.test import TestCase
from account.models import *
from .factories import *


def setUp(self):
        self.user = UserFactory.build()
        self.user.save()
        self.user_profile = UserProfileFactory.build()
        self.user_profile.save()
        self.admin = AdminFactory.build()
        self.admin.save()

