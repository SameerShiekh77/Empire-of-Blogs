from django.contrib import admin
from blog.models import Blog,SubscriberEmail,BlogCategory
from import_export.admin import ImportExportModelAdmin, ExportActionModelAdmin
# Register your models here.

class BlogAdmin(ImportExportModelAdmin, ExportActionModelAdmin,admin.ModelAdmin):
    list_display = ('title','author','no_of_likes','is_latest_blog','created_at')
    search_fields = ('title','author__username')
    prepopulated_fields = {'slug': ('title',)}
    
    list_filter = ('is_latest_blog',)
    autocomplete_fields = ('author',)

admin.site.register(Blog,BlogAdmin)

class SubscriberEmailAdmin(ImportExportModelAdmin, ExportActionModelAdmin,admin.ModelAdmin):
    list_display = ('email','created_at')
    search_fields = ('email',)

admin.site.register(SubscriberEmail,SubscriberEmailAdmin)

class BlogCategoryAdmin(ImportExportModelAdmin, ExportActionModelAdmin,admin.ModelAdmin):
    list_display = ['name','created_at']
    search_fields = ['name']
    prepopulated_fields = {'slug': ['name']}
    
    

admin.site.register(BlogCategory,BlogCategoryAdmin)