from django.db import models
from datetime import datetime

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import Group, Permission


# Create your models here.
# class Registeruser(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=25)
#     email = models.EmailField(unique=True)
#     password = models.TextField()
#     mobileno = models.CharField(max_length=10)
#     image = models.FileField(upload_to="assets/image/")
#     usertype = models.TextField(default="user")
#     date = models.DateTimeField(default=datetime.now)
 
#     def __str__(self): 
#         return self.name



class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, name, mobileno="", image="", usertype="user"):
        if not email:
            raise ValueError('Email is required')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, mobileno=mobileno, image=image, usertype=usertype)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, name, mobileno="", image="", usertype="user"):
        user = self.create_user(email, password, name, mobileno, image, usertype)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user
    



class Registeruser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=25)
    mobileno = models.CharField(max_length=10, blank=True)
    image = models.FileField(upload_to="assets/image/", blank=True)
    usertype = models.TextField(default="user")
    date = models.DateTimeField(default=datetime.now)
    password = models.CharField(max_length=128)  # Adjust the max_length as needed

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = CustomUserManager()

    def __str__(self):
        return self.name

    groups = models.ManyToManyField(Group, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set')
