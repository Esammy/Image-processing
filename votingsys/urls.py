from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.votingTest, name='vote'),
    path('idsearch', views.idSearch, name='idsearch'),
    path('login/', auth_views.LoginView.as_view(template_name = 'login.html'), name= 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'logout.html'), name= 'logout'),
    path('register/', views.register, name= 'register'),
    path('profile/', views.profile, name='profile'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)