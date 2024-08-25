from django.db import models
from django.utils import timezone
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)
    image = models.ImageField(upload_to='category_images')
    slug = models.SlugField(max_length=100,unique=True)
    no_of_store = models.IntegerField(default=0)
    is_popluar = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"
    
class Store(models.Model):
    store_name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=100,unique=True)
    image = models.ImageField(upload_to='store_images')
    description = models.TextField()
    rating = models.IntegerField()
    website_url = models.CharField(max_length=255)
    categories = models.ManyToManyField(Category,blank=True)
    store_of_the_week = models.BooleanField(default=False)
    facebook_link = models.URLField(null=True,blank=True)
    twitter_link = models.URLField(null=True,blank=True)
    gmail = models.EmailField(null=True,blank=True)
    linkedin_link = models.URLField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return self.store_name
    
class Coupon(models.Model):
    coupon_code = models.CharField(max_length=100,null=True,blank=True)
    description = models.CharField(max_length=255)
    store = models.ForeignKey(Store,on_delete=models.CASCADE)
    expiry_date = models.DateField()
    coupon_url = models.CharField(max_length=255)
    featured = models.BooleanField(default=False)
    usage_count = models.IntegerField(default=0)
    is_deal =  models.BooleanField(default=False)
    sort_order  = models.IntegerField(default=1,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return self.coupon_code or "Deal"
    

class MetaTags(models.Model):
    name = models.CharField(max_length=200,null=True, blank=True)
    meta_tag = models.TextField()

    def __str__(self):
        return self.name or "Tags"
    
    class Meta():
        verbose_name_plural = "Head Meta Tags"


class BodyMetaTags(models.Model):
    name = models.CharField(max_length=200,null=True, blank=True)
    meta_tag = models.TextField()

    def __str__(self):
        return self.name or "Tags"
    
    class Meta():
        verbose_name_plural = "Body Meta Tags"


class Bannners(models.Model):
    discount_percentage = models.CharField(max_length=100,null=True,blank=True)
    reviews = models.IntegerField(default=1)
    rating = models.IntegerField(default=1)
    image = models.ImageField(upload_to='headers')
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return str(self.pk)
    

    class Meta():
        verbose_name_plural = "Banners"


class HomePageAdPlacement(models.Model):
    AD_TYPE = (('home_page','home_page'),('coupon_page','coupon_page'))
    ad_name = models.CharField(max_length=200)
    ad_link = models.URLField()
    ad_image = models.FileField(upload_to='home-advert')
    is_active = models.BooleanField(default=False)
    banner_placed_on = models.CharField(max_length=200,null=True,blank=True,choices=AD_TYPE)
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    
    def __str__(self):
        return self.ad_name
    
    class Meta:
        verbose_name = 'Home Page Ad Placement'

class HomePageBanner(models.Model):
    banner_image = models.ImageField(upload_to='home-banner')
    banner_name = models.CharField(max_length=200, null=True, blank=True)
    banner_link = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.banner_name
    
    class Meta:
        verbose_name = 'Home Page Banner'