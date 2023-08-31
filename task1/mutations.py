import graphene
from .fields import PostClass,PostCommentClass,UserClass
from .models import Post,PostComment,User
import graphql_jwt
from graphql_jwt.decorators import permission_required
from graphql_jwt.decorators import login_required







class createPost(graphene.Mutation):
    error = graphene.String()
    success = graphene.Boolean()
    post=graphene.Field(PostClass)
    
    class Meta:
        description='Create Post '

    class Arguments:
        author_id_id=graphene.ID(required=True)
        title=graphene.String(required=True)
        content=graphene.String(required=True)
    
    @login_required
    def mutate(self, info, **kwargs):
        print(info.context.user.pk,'iN post method')
        try:
            usrid=info.context.user.pk
            if usrid == int(kwargs.get('author_id_id')):
                post=Post.objects.create(title=kwargs.get('title'),
                                        content=kwargs.get('content'),
                                        author_id_id=kwargs.get('author_id_id')
                                        )
                return createPost(post=post,success=True)
            else:
                createPost(post=None,success=False)

        except Exception as e:
            return createPost(post=None,success=False,error=e)

class updatePost(graphene.Mutation):
    error = graphene.String()
    success = graphene.Boolean()
    post=graphene.Field(PostClass)
    
    class Meta:
        description='update Post '

    class Arguments:
        
        id = graphene.ID()
        title=graphene.String(required=True)
        content=graphene.String(required=True)
    
    @login_required
    def mutate(self, info, title, content,id):
        try:
            authid=info.context.user.pk
            post=Post.objects.get(id=id ,author_id_id=authid)
            post.title=title
            post.content=content
            post.save()
            return updatePost(post=post,success=True)
        except Exception as e:


            return updatePost(post=None,success=False,error=e)



class createPostComment(graphene.Mutation):
    error = graphene.String()
    success = graphene.Boolean()
    comment = graphene.Field(PostCommentClass)

    class Arguments:
        author_id_id=graphene.ID(required=True)
        post_id_id=graphene.ID(required=True)
        content=graphene.String(required=True)
    
    @login_required
    def mutate(self,info, **kwargs):
        try:
            userid=info.context.user.pk
            print(userid)
            
            if userid==int(kwargs.get('author_id_id')):
                comment=PostComment.objects.create(post_id_id=kwargs.get('post_id_id'),
                                        content=kwargs.get('content'),
                                        author_id_id=kwargs.get('author_id_id')
                                        )
            
                return createPostComment(comment=comment,success=True)
            else:
                return createPostComment(comment=None,success=False)
        
        except Exception as e:
            return createPostComment(comment=None,success=False,error=e)




class updatePostComment(graphene.Mutation):
    error = graphene.String()
    success = graphene.Boolean()
    comment=graphene.Field(PostCommentClass)
    
    class Meta:
        description='update Post comment'

    class Arguments:
        
        id = graphene.ID()
        # title=graphene.String(required=True)
        content=graphene.String(required=True)
    
    # @permission_required('auth.change_user')
    
    @login_required
    def mutate(self, info,  content,id):
        try:
            userid=info.context.user.pk
            comment=PostComment.objects.get(id=id,author_id_id=userid)
            
            comment.content=content
            comment.save()
            return updatePostComment(comment=comment,success=True)
        except Exception as e:


            return updatePostComment(comment=None,success=False,error=e)


class delete(graphene.Mutation):
    error=graphene.String()
    success=graphene.Boolean()

    class Arguments:
        user_id=graphene.ID()
        post_id=graphene.ID()
        comment_id=graphene.ID()
    
    @login_required
    def mutate(self,info,**kwargs):
        try:
            userid=info.context.user.pk
            if kwargs.get('user_id'):
                User.objects.get(id=kwargs.get('user_id')).delete()

            if kwargs.get('post_id'):
                Post.objects.filter(id=kwargs.get('post_id'),author_id_id=userid).delete()

            if kwargs.get('comment_id'):
                PostComment.objects.filter(id=kwargs.get('comment_id'),author_id_id=userid).delete()
            return delete(success=True)  
        except Exception as e:
            return delete(success=False,error=e)

