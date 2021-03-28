from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user1/', include('user1.urls')),
    path('admin1/', include('admin1.urls')),
    path('hirer/', include('hirer.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
