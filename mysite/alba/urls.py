from django.urls import include, path, re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    re_path(r'^ajax/dadosdeputados', views.DadosDeputadoView, name='deputados'),
    path('', views.IndexView, name='index'),
    path('<str:slug>', views.IndexView, name='index'),
    path('<str:slug>/<str:ano>', views.IndexView, name='index'),
    path('<str:slug>/<str:ano>/<str:mes>', views.IndexView, name='index'),
]
