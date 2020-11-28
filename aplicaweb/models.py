from django.db import models

# Create your models here.

class descuento(models.Model):
    numdefactura = models.IntegerField (max_length=43)
    nombre = models.CharField (max_length=40)
    infdefactura = models.CharField (max_length=64)
    usuario = models.CharField (max_length=45)
    clave = models.CharField(max_length= 20, blank= False, null= False)


class servicio_factura(models.Model):
    nom_de_factura = models.CharField (max_length=43)
    num_defacrura = models.CharField (max_length=40)
    fecha_de_corte = models.DateField(null=True)
    fecha_de_pago = models.DateField(null=True)
    descripcion_fac = models.CharField (max_length=54)

    

class tarjeta_de_credito(models.Model):

    GENDER_CHOICES = (

        ('C', 'CREDITO'),
        ('D', 'DEBITO'),
    )

    tipo_de_tarjeta = models.CharField(max_length=1, choices=GENDER_CHOICES)
    fecha_de_vencimiento = models.DateField(null=True)
    plazo = models.IntegerField (max_length=64)
    num_de_cuenta = models.IntegerField(max_length=8, verbose_name='Numero_de_cuenta')
    
    GENDER_CHOICES = (

        ('S', 'SI'),
        ('N', 'NO'),
    )
    
    disponible = models.CharField(max_length=1, choices=GENDER_CHOICES)



