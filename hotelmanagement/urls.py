
from django.contrib import admin
from django.urls import path , include
from accounts import urls as accounts_urls
from hotels import urls as hotels_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(hotels_urls)),
    path('accounts/', include(accounts_urls)),
]
