
from django.urls import path
from .views import blog_detail, subscriber_email,category


urlpatterns = [
    path('category/<slug:slug>/',category,name='category'),
    path('blog-detail/<slug:slug>/',blog_detail,name='blog-detail'),
    path('subscriber-email/',subscriber_email,name='subscriber-email'),
]