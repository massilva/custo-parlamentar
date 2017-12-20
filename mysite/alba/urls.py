from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path('', views.IndexView, name='index'),
    re_path('(?P<slug>)', views.IndexView, name='index'),
    # path('<deputado_id>', views.DeputadoView, name='deputado'),
]
