from django.shortcuts import render,redirect
from blog.models import Blog, BlogCategory, SubscriberEmail

def blog_detail(request,slug):
    
    blog = Blog.objects.filter(slug=slug).first()
    navigation = BlogCategory.objects.all()[:5]
    
    context = {
        'blog':blog,
        'navigation':navigation
        
    }
    return render(request,'blog-detail.html',context)

def subscriber_email(request):
    if request.method == 'POST':
        email = request.POST.get('user_email')
        try: 
            SubscriberEmail.objects.create(email=email)
        except Exception as e:
            pass
        return redirect('index')
        