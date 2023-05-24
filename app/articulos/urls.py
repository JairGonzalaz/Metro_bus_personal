from django.urls import path, include 
from django.contrib.auth import views as auth_views

from articulos.views import Articulo
urlpatterns = [
    path('articulos/',Articulo.as_view(template_name='articulo/articulos_list.html'),name='articulos'),
]
