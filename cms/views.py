from django.shortcuts import render, redirect
from blog.models import Blog, BlogCategory, Contact
from .models import Store
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
def impressum_page(request):
    return render(request,'impressum.html')
def contact_form_submit(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        user_email = request.POST.get('user_email')
        user_subject = request.POST.get('user_subject')
        user_message = request.POST.get('user_message')
        print("user_name,", user_email)
        # Create and save the contact form submission
        contact = Contact(
            user_name=user_name,
            user_email=user_email,
            user_subject=user_subject,
            user_message=user_message,
        )
        contact.save()

        return redirect('impressum')
def stores(request):
    stores = Store.objects.all()
    navigation = BlogCategory.objects.all()[:5]
    context = {
        'stores':stores,
        'navigation':navigation
    }
    return render(request,'stores.html',context)