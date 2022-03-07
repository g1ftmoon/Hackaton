from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from shmot_shop import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('applications.account.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
