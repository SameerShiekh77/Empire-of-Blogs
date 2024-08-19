from django.shortcuts import render,redirect
from blog.models import Blog, BlogCategory, SubscriberEmail

def blog_detail(request,slug):
    
    blog = Blog.objects.filter(slug=slug).first()
    navigation = BlogCategory.objects.all()[:5]
    recommend_blogs = Blog.objects.all().order_by("?")[:3]
    
    context = {
        'blog':blog,
        'navigation':navigation,
        "recommend_blogs":recommend_blogs
        
    }
    return render(request,'blog-detail.html',context)

def subscriber_email(request):
    if request.method == 'POST':
        email = request.POST.get('user_email')
        try: 
            SubscriberEmail.objects.create(email=email)
        except Exception as e:
            pass
        # return render(request, 'index.html', {'subscribed': subscribed})
        return redirect('index')

        
        
def category(request,slug):
    navigation = BlogCategory.objects.all()[:5]
    all_blogs = Blog.objects.all()
    blogs = all_blogs.filter(blog_category__slug=slug)
    featured_blogs = all_blogs.filter(is_featured_blog=True)
    recent_blogs = all_blogs.all().order_by('-created_at')
    context = {
        'navigation':navigation,
        "blogs":blogs,
        'featured_blogs':featured_blogs,
        "recent_blogs":recent_blogs
        
    }
    return render(request,'blog-category.html',context)