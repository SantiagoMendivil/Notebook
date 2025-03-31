from django.contrib.contenttypes.fields import GenericForeignKey 
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    
    """other fiels"""
    
    
class BlogPost(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.URLField()
    app = models.CharField(max_length=200)
    message = models.TextField(max_length=400)
    
""" 
    Suppose we have the two models above. The comment must be abstract because it can appear in a blogpost
    or an article, or a notification, so it must be related to more than one mode in order to save information
    about that related model. Meaning that for example:
        comment.blogpost.url 
    Must access the information about that specific model. 
    
    If an instance of BlogPost is created, then the code would be: 
"""
from django.contrib.contenttypes.models import ContentType
from .models import Comment, BlogPost

blog_post = BlogPost.objects.get(id=1)

comment = Comment.objects.create(
    content_type=ContentType.objects.get_for_model(BlogPost),
    object_id=blog_post.id, 
    url="someurl.com",
    message="This is a comment",
)