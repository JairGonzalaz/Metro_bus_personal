from django.shortcuts import render
from django.views import generic

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Autor

# Create your views here.

class AutorView(LoginRequiredMixin,generic.CreateView):
    model = Autor
    template_name = "autores/cards_autores.html"
    context_object_name="obj" 
    login_url = 'bases:login'
    fields = ['nombre']

