from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    email = models.EmailField(max_length=254, unique=True, db_index=True, blank=True)
    name = models.CharField(max_length=254, blank=True,null=True)
    USERNAME_FIELD = 'email'
    def get_username(self):
        return self.email

    # REQUIRED_FILEDS = ['username']
