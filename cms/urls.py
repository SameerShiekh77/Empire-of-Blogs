from django.urls import path,include
from .views import index, about_us, terms_and_conditions, privacy_policy, terms_of_use, impressum_page,contact_form_submit, stores, show_categories, category_detail, store_detail, coupon_list
from froala_editor import views
urlpatterns = [
    path('froala_editor/',include('froala_editor.urls')),
    path('',index,name='index'),
    path('privacy-policy/',privacy_policy,name='privacy-policy'),
    path('terms-and-conditions/',terms_and_conditions,name='terms-and-conditions'),
    path('terms-of-use/',terms_of_use,name='terms-of-use'),
    path('about-us/',about_us,name='about-us'),
    path('impressum/', impressum_page,name='impressum'),
    path('contact/', contact_form_submit, name='contact'),
    path('stores/',stores,name='stores'),
    path('stores/category/<slug:category_slug>/', stores, name='category_stores'),
    path('categories/',show_categories,name='categories'),
    path('category/<slug:slug>/', category_detail, name='category_detail'),
    path('store/<slug:slug>/', store_detail, name='store_detail'),
    path('coupon-list/', coupon_list, name='coupon-list')  
]