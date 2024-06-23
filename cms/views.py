from django.shortcuts import render
from blog.models import Blog, BlogCategory
# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    navigation = BlogCategory.objects.all()[:5]
    context = {
        'blogs':blogs,
        'navigation':navigation
    }
    return render(request,'index.html',context)


def about_us(request):
    navigation = BlogCategory.objects.all()[:5]
    context = {
        'navigation':navigation
    }
    return render(request,'about.html',context)

def terms_and_conditions(request):
    navigation = BlogCategory.objects.all()[:5]
    context = {
        'navigation':navigation
    }
    return render(request,'terms-and-conditions.html',context)

def terms_of_use(request):
    navigation = BlogCategory.objects.all()[:5]
    context = {
        'navigation':navigation
    }
    return render(request,'terms_of_use.html',context)


def privacy_policy(request):
    navigation = BlogCategory.objects.all()[:5]
    context = {
        'navigation':navigation
    }
    return render(request,'privacy.html',context)