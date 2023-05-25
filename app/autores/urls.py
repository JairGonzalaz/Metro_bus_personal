from django.urls import path

from .views import AutorView

urlpatterns = [
    path('autores/', AutorView.as_view(template_name="autores/cards_autores.html"),name='autores'),

]
