
from django.contrib import admin
from django.urls import path , include
from accounts import urls as accounts_urls
from hotels import urls as hotels_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(hotels_urls)),
    path('accounts/', include(accounts_urls)),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)