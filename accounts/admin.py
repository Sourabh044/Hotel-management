from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import *
from hotels.models import *
# Register your models here.
admin.site.site_header = 'Hotel Management'
admin.site.site_title = 'HMS'
admin.site.site_title = "HMS"
admin.site.index_title = "Hotel Management System Project"

class HotelImagesInline(admin.StackedInline):
    model = HotelImages
    readonly_fields = ('deleted_at',)
    fields = ('image','uploaded_by')


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # ordering = ('created_at',)
    readonly_fields = ('date_joined','last_login',)


@admin.register(Hotel)
class Hoteladmin(admin.ModelAdmin):
    readonly_fields = ('deleted_at',)
    inlines = (HotelImagesInline,)

admin.site.register(HotelImages)