from django.db import models

# Create your models here.

class descuento(models.Model):
    numdefactura = models.IntegerField (max_length=43)
    nombre = models.CharField (max_length=40)
    infdefactura = models.CharField (max_length=64)
    usuario = models.CharField (max_length=45)
    clave = models.CharField(max_length= 20, blank= False, null= False)


class pago(models.Model):
    fecha_de_pago = models.DateField (auto_now_add=True)
    forma_de_pago = models.CharField (max_length=50, verbose_name='Forma de pago')
    num_de_operacion = models.IntegerField (max_length=64)
    tipo_de_cuenta = models.CharField (max_length=45)
    monto = models.DecimalField(max_digits=7, decimal_places=2)


    


class cliente(models.Model):
    nombre = models.CharField (max_length=50)
    direccion = models.CharField (max_length=40)
    telefono = models.CharField (max_length=64)
    email = models.EmailField()
    GENDER_CHOICES = (

        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    sexo = models.CharField(max_length=1, choices=GENDER_CHOICES)
    ciudad = models.CharField (max_length=50)
    estado = models.CharField (max_length=40)


class usuario(models.Model):
    nombre = models.CharField (max_length=50)
    apellido = models.CharField (max_length=40)
    username = models.CharField(max_length=100)
    contraseña = models.CharField(max_length= 20, blank= False, null= False)
    email = models.EmailField(max_length=100)


class tarjeta_de_credito(models.Model):

    GENDER_CHOICES = (

        ('C', 'CREDITO'),
        ('D', 'DEBITO'),
    )

    tipo_de_tarjeta = models.CharField(max_length=1, choices=GENDER_CHOICES)
    fecha_de_vencimiento = models.DateField(null=True)
    plazo = models.IntegerField (max_length=64)
    num_de_cuenta = models.IntegerField(max_length=8, verbose_name='Numero de cuenta')
    
    GENDER_CHOICES = (

        ('S', 'SI'),
        ('N', 'NO'),
    )
    
    disponible = models.CharField(max_length=1, choices=GENDER_CHOICES)




class servicio_factura(models.Model):
    nom_de_factura = models.CharField (max_length=43)
    numdefacrura = models.IntegerField (max_length=40)
    fecha_de_corte = models.DateField(null=True)
    fecha_de_pago = models.DateField(null=True)
    descripcion_fac = models.CharField (max_length=54)
    
    