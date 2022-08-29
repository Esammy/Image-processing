from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'image_compression'

urlpatterns = [
    path('', views.kmeans, name='kmeans'),
    path('dwt/', views.dwt, name='dwt'),
    #path('success/', views.success, name='success'),
    #path('transform/', views.display_images, 'transform')
]

