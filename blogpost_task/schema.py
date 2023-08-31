import graphene
from graphene_django import DjangoObjectType
from task1.models import User,Post,PostComment

import graphql_jwt

from graphql_jwt.decorators import permission_required
from graphql_jwt.decorators import login_required


from graphql_auth.schema import UserQuery,MeQuery
from graphql_auth import mutations



from task1.mutations import createPostComment,createPost,updatePost,updatePostComment,delete
from task1.fields import PostClass,PostCommentClass,UserClass

class AuthMutation(graphene.ObjectType):
   register = mutations.Register.Field()
   verify_account = mutations.VerifyAccount.Field()
   token_auth = mutations.ObtainJSONWebToken.Field()
   # verify_token = mutations.Verify.Field()
   # refresh_token = mutations.Refresh.Field()




class Query(UserQuery,MeQuery,graphene.ObjectType):
   userslist=graphene.List(UserClass)
   userid=graphene.Field(UserClass,id=graphene.Int())
   blogposts=graphene.List(PostClass)
   readpost=graphene.Field(PostClass,id=graphene.Int())

   comments=graphene.List(PostCommentClass)
   readcomment=graphene.Field(PostCommentClass,id=graphene.ID())


   def resolve_userslist(root,info):
      
      return User.objects.all()
   
   def resolve_userid(root,info,id):
      return User.objects.get(id=id)

   @login_required 
   def resolve_blogposts(root,info):
      print(info.context.user.pk,'userrrr')
      return Post.objects.all()

   @login_required 
   def resolve_readpost(root,info,id):
      return Post.objects.get(id=id)
   
   @login_required
   def resolve_comments(root,info):
      return PostComment.objects.all()

   @login_required
   def resolve_readcomment(root,info,id):
      return PostComment.objects.get(id=id)


class Mutation(AuthMutation, graphene.ObjectType):
   create_post=createPost.Field()
   update_post=updatePost.Field()
   create_post_comment=createPostComment.Field()
   update_post_comment=updatePostComment.Field()
   delete=delete.Field()


schema=graphene.Schema(query=Query,mutation=Mutation)






    
      




