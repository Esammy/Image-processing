from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('image_compression.urls', namespace='image_compression')),
    path('votingsys/', include('votingsys.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
                           document_root=settings.MEDIA_ROOT)