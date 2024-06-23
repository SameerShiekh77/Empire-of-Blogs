from django.shortcuts import render
from blog.models import Blog, BlogCategory

def blog_detail(request,slug):
    
    blog = Blog.objects.filter(slug=slug).first()
    navigation = BlogCategory.objects.all()[:5]
    
    context = {
        'blog':blog,
        'navigation':navigation
        
    }
    return render(request,'blog-detail.html',context)