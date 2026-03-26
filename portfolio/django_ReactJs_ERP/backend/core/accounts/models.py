from django.db import models
from django.contrib.auth.models import AbstractBaseUser, Permission

from companies.models import Enterprise

# Create your models here.
class User(AbstractBaseUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    is_owner = models.BooleanField(default=True)

    #Campo resposnavel pelo username
    USERNAME_FIELD = 'email'

    def __str__(self) -> str:
        return self.email
    

class Group(models.Model):
    name =  models.CharField(max_length=50)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE, related_name='groups')


class GroupPermission(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='permissions')
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE, related_name='group_permissions')


class UserGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_groups')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='user_groups')