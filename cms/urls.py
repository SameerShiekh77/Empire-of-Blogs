from django.urls import path,include
from .views import index
from froala_editor import views
urlpatterns = [
    path('froala_editor/',include('froala_editor.urls')),
    path('',index,name='index'),
    # path('privacy-policy/',privacy_policy,name='privacy-policy'),
    # path('terms-and-conditions/',terms_and_conditions,name='terms-and-conditions'),
    # path('about-us/',about_us,name='about-us'),
    # path('categories/',categories,name='categories'),
    # path('category-detail/<slug:slug>/',category_detail,name='category-detail'),
    # path('stores/',stores,name='stores'),
    # path('store-detail/<slug:slug>/',store_detail,name='store-detail'),
    # path('get_search_suggestions/', get_search_suggestions, name='get_search_suggestions'),
]