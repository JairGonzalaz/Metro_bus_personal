from django.shortcuts import render


from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
# Create your views here.

class Articulo(LoginRequiredMixin,generic.TemplateView):
    template_name = 'articulo/articulos_list.html'
    articulo_url = 'articulo:articulos'

# Create your views here.
