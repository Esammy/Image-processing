from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.votingTest, name='vote'),
    path('idsearch', views.idSearch, name='idsearch'),
]