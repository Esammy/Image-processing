from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'image_compression'

urlpatterns = [
    path('', views.dwt, name='img_upload'),
    path('kmeans/', views.kmeans, name='kmeans'),
    path('dwtparameters', views.dwtparameters, name='dwtparameters'),
    #path('dwt/', views.display_images, 'transform')
]

