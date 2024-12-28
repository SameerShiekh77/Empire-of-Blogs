from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import BlogSitemap, CategorySitemap
from django.conf import settings
from django.conf.urls.static import static

sitemaps = {
    'blogs': BlogSitemap,
    'categories': CategorySitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cms.urls')),
    path('blogs/', include('blog.urls')),
    path("__reload__/", include("django_browser_reload.urls")),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Empire of Blogs'
admin.site.site_title = 'Empire of Blogs'
admin.site.index_title = 'Empire of Blogs'
