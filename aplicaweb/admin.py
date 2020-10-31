from django.contrib import admin

from .models import descuento

class descuentoadmin(admin.modeladmin):
    pass

# Register your models here.
admin.site.register(descuento,descuentoadmin)