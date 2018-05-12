from django.db import models
from django.contrib import auth
from django.urls import reverse
# Create your models here.
class User(auth.models.User,auth.models.PermissionsMixin):
    def __str__(self):
        return "@{}".format(self.username) #username is bulit-in

    def get_absolute_url(self):
        return  reverse('accounts:login/',kwargs={"id":self.id}) 
