
from django.urls import path
from .views import blog_detail, subscriber_email


urlpatterns = [
    # path('',blog_page,name='blogs'),
    path('blog-detail/<slug:slug>/',blog_detail,name='blog-detail'),
    path('subscriber-email/',subscriber_email,name='subscriber-email')
]