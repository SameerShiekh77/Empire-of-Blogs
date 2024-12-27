from django.contrib import admin
from cms.models import Category, Store, Coupon, MetaTags, BodyMetaTags, Bannners,HomePageAdPlacement, HomePageBanner, StorePageBanner, AccessUrls
from import_export.admin import ImportExportModelAdmin, ExportActionModelAdmin
from django.db.models import Max
from import_export import resources
from django.shortcuts import redirect
from django.utils.html import format_html
from django.urls import path
# Register your models here.

class CategoryAdmin(ImportExportModelAdmin, ExportActionModelAdmin,admin.ModelAdmin):
    list_display = ('name','slug','created_at')
    search_fields = ('name','slug')
    readonly_fields = ('no_of_store',)
    prepopulated_fields = {'slug':('name',)} 

    # resource_class = InstructorCommissionResource
    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)

    #     if request.user.is_superuser:
            
    #         return qs

    #     elif request.user.is_staff:
    #         # For staff users, filter records based on the user's ID
    #         qs = qs.filter(instructor__name=request.user)
    #     return qs
    
    # def changelist_view(self, request, extra_context=None):
    #     extra_context = extra_context or {}
    #     extra_context['total_records'] = InstructorCommission.objects.filter(instructor__name=request.user).count()
    #     extra_context['allow'] = True

    #     total_commission = 0
    #     queryset = InstructorCommission.objects.filter(instructor__name=request.user)
    #     for obj in queryset:
    #         total_commission += obj.commission()  # Replace with the actual method name

    #     extra_context['total_commission'] = total_commission
    #     return super().changelist_view(request, extra_context=extra_context)


class StoreAdmin(ImportExportModelAdmin, ExportActionModelAdmin,admin.ModelAdmin):
    list_display = ('store_name','slug','rating','created_at')
    search_fields = ('store_name','slug')
    filter_horizontal = ('categories',)
    prepopulated_fields = {'slug': ('store_name',)}
    

class CouponAdmin(ImportExportModelAdmin, ExportActionModelAdmin,admin.ModelAdmin):
    list_display = ('coupon_code','sort_order','description','store','is_deal','expiry_date','created_at')
    search_fields = ('coupon_code','store__store_name')
    list_filter = ('is_deal','store__store_name')
    autocomplete_fields = ('store',)
    list_editable = ['sort_order']
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj is None:
            last_sort_order = Coupon.objects.aggregate(max_sort_order=Max('sort_order'))['max_sort_order']
            next_sort_order = (last_sort_order or 0) + 1
            form.base_fields['sort_order'].initial = next_sort_order
        return form
    def save_model(self, request, obj, form, change):
        if not obj.pk: 
            last_id = Coupon.objects.aggregate(max_id=Max('id'))['max_id']
            next_id = (last_id or 0) + 1
            obj.id = next_id  
        super().save_model(request, obj, form, change)

class BannerAdmin(ImportExportModelAdmin, ExportActionModelAdmin,admin.ModelAdmin):
    list_display = ['discount_percentage','reviews','rating']
    list_filter = ['rating']
    readonly_fields = ['created_at']

class HomePageBannerAdmin(admin.ModelAdmin):
    list_display = ('banner_name', 'banner_link', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('banner_name', 'banner_link')
class StorePageBannerAdmin(admin.ModelAdmin):
    list_display = ('banner_name', 'banner_link', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('banner_name', 'banner_link')
class StoreAccessAdmin(admin.ModelAdmin):
    list_display = ('name', 'full_url', 'updated_at', 'regenerate_button')

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        readonly_fields = readonly_fields + ('unique_key',)
        return readonly_fields
    def get_urls(self):
        """Add a custom URL for the regenerate action."""
        urls = super().get_urls()
        custom_urls = [
            path(
                '<int:object_id>/regenerate/',
                self.admin_site.admin_view(self.regenerate_key),
                name='regenerate_key',
            ),
        ]
        return custom_urls + urls

    def regenerate_key(self, request, object_id):
        """Regenerate the unique key for a specific object."""
        try:
            obj = AccessUrls.objects.get(pk=object_id)
            obj.regenerate_key()
            self.message_user(request, f"Key regenerated for {obj.full_url}.")
        except AccessUrls.DoesNotExist:
            self.message_user(request, f"Access URL with ID {object_id} does not exist.", level='error')
        return redirect('admin:cms_accessurls_changelist')

    def regenerate_button(self, obj):
        """Generate a button to regenerate the key for each object."""
        return format_html(
            '<a class="button" href="{}/regenerate/">Regenerate Key</a>',
            obj.pk,
        )
    regenerate_button.short_description = "Regenerate Key"
    regenerate_button.allow_tags = True


admin.site.register(AccessUrls, StoreAccessAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Store,StoreAdmin)
admin.site.register(Coupon,CouponAdmin)
admin.site.register(MetaTags)
admin.site.register(BodyMetaTags)
admin.site.register(HomePageAdPlacement)
admin.site.register(HomePageBanner, HomePageBannerAdmin)
admin.site.register(StorePageBanner, StorePageBannerAdmin)
# admin.site.register(Bannners,BannerAdmin)