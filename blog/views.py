from django.shortcuts import render,redirect
from django.shortcuts import render, get_object_or_404
from blog.models import Blog, BlogCategory, SubscriberEmail
from django.utils.html import strip_tags

def blog_detail(request, slug):
    blog = Blog.objects.filter(slug=slug).first()
    navigation = BlogCategory.objects.all()[:5]
    recommend_blogs = Blog.objects.all().order_by("?")[:3]
    processed_blogs = []
    
    for b in recommend_blogs:
        description_plain = strip_tags(b.description)[:200] + "..." if len(strip_tags(b.description)) > 100 else strip_tags(b.description)
        b.description_plain = description_plain 
        processed_blogs.append(b)
    
    context = {
        'blog': blog,
        'navigation': navigation,
        'recommend_blogs': processed_blogs 
    }
    
    return render(request, 'blog-detail.html', context)


def subscriber_email(request):
    if request.method == 'POST':
        email = request.POST.get('user_email')
        try: 
            SubscriberEmail.objects.create(email=email)
        except Exception as e:
            pass
        # return render(request, 'index.html', {'subscribed': subscribed})
        return redirect('index')

        
        
def category(request, slug):
    category = get_object_or_404(BlogCategory, slug=slug)
    navigation = BlogCategory.objects.all()[:5]
    all_blogs = Blog.objects.all()
    blogs = all_blogs.filter(blog_category__slug=slug)
    featured_blogs = all_blogs.filter(is_featured_blog=True)[:5]
    recent_blogs = all_blogs.all().order_by('-created_at')[:5]
    processed_blogs = []
    for blog in blogs:
        blog.description_plain = strip_tags(blog.description)[:250] + "..." if len(strip_tags(blog.description)) > 100 else strip_tags(blog.description)
        processed_blogs.append(blog)

    context = {
        'navigation': navigation,
        "blogs": processed_blogs,
        'featured_blogs': featured_blogs,
        "recent_blogs": recent_blogs,
        'category_name': category.name,
    }
    return render(request, 'blog-category.html', context)