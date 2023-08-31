from django.db import models
from django.contrib.auth.models import AbstractBaseUser,UserManager,AbstractUser

from django.utils.translation import gettext_lazy as _

# Create your models here.


class User(AbstractUser):
    objects=UserManager()
    username=models.CharField(max_length=80,unique=True)
    email=models.CharField(max_length=100,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']



class Post(models.Model):
    author_id=models.ForeignKey(User,related_name="user",on_delete=models.CASCADE)
    title=models.CharField(max_length=60)
    content=models.CharField(max_length=130,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PostComment(models.Model):
    author_id=models.ForeignKey(User,on_delete=models.CASCADE)
    post_id=models.ForeignKey(Post,related_name='post',on_delete=models.CASCADE)
    content=models.CharField(max_length=130,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
