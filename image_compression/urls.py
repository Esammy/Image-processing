from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.conf.urls import url
from django.views.static import serve

app_name = 'image_compression'

urlpatterns = [
    path('', views.home, name='home'),
    path('dwt', views.dwt, name='dwt'),
    path('filters', views.filters, 'filters'),
    path('kmeans', views.kmeans, name='kmeans'),
    path('dwtparameters', views.dwtparameters, name='dwtparameters'),
    path('catoonsketch', views.catoonsketch, name='catoonsketch'),
    path('sketch', views.sketch, name='sketch'),
    

    path('workspace', views.work, name='workspace1'),
    path('formtest', views.formtest, name='formtest'),
    

    url(r'^download_image/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT})
]

