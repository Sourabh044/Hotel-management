from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import *
from hotels.models import *
# Register your models here.
admin.site.site_header = 'Hotel Management'
admin.site.site_title = 'HMS'
admin.site.site_title = "HMS"
admin.site.index_title = "Hotel Management System Project"

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # ordering = ('created_at',)
    readonly_fields = ('date_joined','last_login',)


admin.site.register(Hotel)
admin.site.register(HotelImages)