from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Blog, BlogCategory


class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1

    def items(self):
        return Blog.objects.all()

    def lastmod(self, obj):
        return obj.created_at

    def location(self, obj):
        return reverse("blog-detail", kwargs={"slug": obj.slug})


class CategorySitemap(Sitemap):
    changefreq = "daily"
    priority = 1

    def items(self):
        return BlogCategory.objects.all()

    def location(self, obj):
        return f"/blogs/category/{obj.slug}/"
