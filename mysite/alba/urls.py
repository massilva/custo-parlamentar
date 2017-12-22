from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path('', views.IndexView, name='index'),
    path('<str:slug>', views.IndexView, name='index'),
]
