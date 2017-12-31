from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path('', views.IndexView, name='index'),
    path('<str:slug>', views.IndexView, name='index'),
    path('<str:slug>/<str:ano>', views.IndexView, name='index'),
    path('<str:slug>/<str:ano>/<str:mes>', views.IndexView, name='index'),
    path('dados/<str:slug>/<str:ano:>', views.DadosDeputadoView, name='deputados')
]
