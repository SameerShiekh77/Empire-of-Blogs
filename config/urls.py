
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('cms.urls')),
    path('blogs/',include('blog.urls')),
]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Empire of Blogs'
admin.site.site_title = 'Empire of Blogs'
admin.site.index_title = 'Empire of Blogs'