from django.db import models

from bases.models import ClaseModelo

# Create your models here.

class Categoria(ClaseModelo):
    descripccion = models.CharField(
        max_length=100,
        help_text='Descripccion de categoria',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripccion)
    
    def save(self):
        self.descripccion = self.descripccion.upper()
        super(Categoria,self).save()

    class Meta:
        verbose_name_plural="Categorias"
