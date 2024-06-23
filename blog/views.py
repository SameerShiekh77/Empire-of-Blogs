from django.shortcuts import render
from blog.models import Blog

def blog_detail(request,slug):
    
    blog = Blog.objects.filter(slug=slug).first()
    
    context = {
        'blog':blog
    }
    return render(request,'blog-detail.html',context)