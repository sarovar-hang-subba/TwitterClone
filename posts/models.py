from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Post(models.Model):
    class Meta(object):
       db_table = 'posts'

    name = models.CharField(
        'name', blank = False, null=False, max_length=14,db_index=True,default='Anonymous'
    ) 
    body=  models.CharField(
        'body', blank = False, null=False, max_length=140,db_index=True
    )
    created_at = models.DateTimeField(
        'Created DateTime', blank=True,auto_now_add=True
    )
    email = models.CharField(
        'email', blank = False, null = False, max_length=20
    )
    likes = models.IntegerField(
        'Likes' , default=0, blank=True
    )
    image = CloudinaryField(
        'image', blank= True, db_index= True
    )
