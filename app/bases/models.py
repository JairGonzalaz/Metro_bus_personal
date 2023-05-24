from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True)#estado activo/inactivo
    fc = models.DateTimeField(auto_now_add=True)#fecha creacion 
    fm = models.DateTimeField(auto_now=True)# fecha modificacion
    uc = models.ForeignKey(User,on_delete=models.CASCADE)#usuario crea
    um = models.IntegerField(blank=True,null=True)#usuario que esta logeado modifica

    class Meta:
        abstract=True


