from django.db import models
from bases.models import ClaseModelo
from django.contrib.auth.models import User

class Categoria(ClaseModelo):
    uc = models.ForeignKey(User, related_name='categorias_articulos', on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=100,
        help_text='descripción de la categoría',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save()

    class Meta:
        verbose_name_plural = "Categorías"
