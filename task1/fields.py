import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import User,Post,PostComment


class UserClass(DjangoObjectType):
    class Meta:
        model=User
        fields=("id","username","email","created_at","updated_at")


class PostClass(DjangoObjectType):
    class Meta:
        model= Post
        fields=("id","title","content","author_id","created_at","updated_at",)


class PostCommentClass(DjangoObjectType):
    class Meta:
        model=PostComment
        fields="__all__"