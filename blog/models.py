from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from django.utils.timezone import datetime
# Create your models here.

class BlogCategory(models.Model):
    name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=100,unique=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Blog Categories"

class Blog(models.Model):
    title = models.CharField(max_length=220,unique=True)
    description = FroalaField()
    slug = models.SlugField(max_length=100,unique=True)
    image = models.ImageField(upload_to='blog_images')
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    blog_category = models.ForeignKey(BlogCategory,blank=True,null=True,on_delete=models.SET_NULL)
    no_of_likes = models.IntegerField(default=0)
    is_latest_blog = models.BooleanField(default=False)
    buy_now_button_link = models.CharField(max_length=225,null=True,blank=True)
    is_buy_now_button_enabled = models.BooleanField(default=False,null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title
    

class SubscriberEmail(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return self.email