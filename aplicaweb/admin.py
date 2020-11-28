from django.contrib import admin

from .models import descuento, servicio_factura, tarjeta_de_credito

class descuentoAdmin(admin.ModelAdmin):
    pass

# Register your models here.

admin.site.register(descuento, descuentoAdmin)
admin.site.register(servicio_factura)
admin.site.register(tarjeta_de_credito)

