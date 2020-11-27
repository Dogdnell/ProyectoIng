from django.contrib import admin

from .models import descuento, pago, cliente, usuario, tarjeta_de_credito, servicio_factura

class descuentoAdmin(admin.ModelAdmin):
    pass

# Register your models here.

admin.site.register(descuento, descuentoAdmin)
admin.site.register(pago)
admin.site.register(cliente)
admin.site.register(usuario)
admin.site.register(tarjeta_de_credito)
admin.site.register(servicio_factura)