from django.db import models

from bases.models import ClaseModelo

# Create your models here.

class Autor(ClaseModelo):
    nombre = models.CharField(
        max_length=100,
        default ='anonimo'
        )
    
    
    
    
    def __str__(self):
        return '()'.format(self.nombre)
    
    def save(self):
        self.nombre = self.nombre.upper()
        super(Autor,self).save()

    class Meta:
        verbose_name_plural = "Autores"
