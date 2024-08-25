from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Blog, BlogCategory, Contact
from .models import Store,Category, Coupon, HomePageAdPlacement, HomePageBanner
from django.http import JsonResponse
# Create your views here.
def index(request):
    home_ad = HomePageAdPlacement.objects.filter(is_active=True,banner_placed_on='home_page').first()
    banners = HomePageBanner.objects.all()
    blogs = Blog.objects.all()
    navigation = BlogCategory.objects.all()[:5]
    context = {
        'blogs':blogs,
        'navigation':navigation,
        'banners': banners,
        "home_ad":home_ad
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
    navigation = BlogCategory.objects.all()[:5]
    context = {
        'navigation':navigation
    }
    
    return render(request,'impressum.html',context)
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
# def newsletter_form_submit(request):
#     subscribed = False
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         print("email,", email)
#         # Create and save the newsletter subscription
#         newsletter = Newsletter(
#             email=email,
#         )
#         newsletter.save()
#         subscribed = True
#         return render(request, 'index.html', {'subscribed': subscribed})
def stores(request, category_slug=None):
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        stores = Store.objects.filter(categories=category)
    else:
        stores = Store.objects.all()
    
    navigation = BlogCategory.objects.all()[:5]
    context = {
        'stores': stores,
        'navigation': navigation,
        'category': category if category_slug else None,
    }
    return render(request, 'stores.html', context)
def show_categories(request):
    categories = Category.objects.all()
    navigation = BlogCategory.objects.all()[:5]
    context = {
        'categories':categories,
        'navigation':navigation
    }
    print(categories)
    return render(request,'categories.html',context)



def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    context = {
        'category': category
    }
    return render(request, 'category_detail.html', context)


def store_detail(request, slug):
    store = get_object_or_404(Store, slug=slug)
    coupons = Coupon.objects.filter(store=store)
    stores = Store.objects.all().order_by("?")[:12]
    navigation = BlogCategory.objects.all()[:5]
    context = {
        'store': store,
        'navigation':navigation,
        'coupons': coupons,
        "stores":stores
    }
    return render(request, 'store_detail.html', context)
def coupon_list(request):
    coupons_ad = HomePageAdPlacement.objects.filter(is_active=True,banner_placed_on='coupon_page').first()
    
    coupon = Coupon.objects.all()
    categoreis = Category.objects.filter(is_popluar=True)
    navigation = BlogCategory.objects.all()[:5]
    
    context = {
        'coupons': coupon,
        'navigation':navigation,
        'categoreis': categoreis,
        "coupons_ad":coupons_ad
    }
    return render(request, 'coupon.html', context)

def search(request):
    query = request.GET.get('search', '')
    if query:
        stores = Store.objects.filter(store_name__icontains=query)
        results = [{'slug': store.slug, 'name': store.store_name} for store in stores]
        return JsonResponse(results, safe=False)
    return JsonResponse([], safe=False)