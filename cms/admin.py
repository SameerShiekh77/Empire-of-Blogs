from django.contrib import admin
from cms.models import Category, Store, Coupon, MetaTags, BodyMetaTags, Bannners
from import_export.admin import ImportExportModelAdmin, ExportActionModelAdmin
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

class BannerAdmin(ImportExportModelAdmin, ExportActionModelAdmin,admin.ModelAdmin):
    list_display = ['discount_percentage','reviews','rating']
    list_filter = ['rating']
    readonly_fields = ['created_at']



admin.site.register(Category,CategoryAdmin)
admin.site.register(Store,StoreAdmin)
admin.site.register(Coupon,CouponAdmin)
admin.site.register(MetaTags)
admin.site.register(BodyMetaTags)
# admin.site.register(Bannners,BannerAdmin)