from django.db import models

# Create your models here.

class descuento(models.model):
    numdefactura = models.charfield(max lengeth=34)
    nombre = models.charfield(max lengeth=40)
    infdefactura = models.charfield(max lendeth=64)
    usuario = models.charfield(max lengeth=45)
    clave = models.integerfield(max lengeth=25)
