from django.contrib import admin
from .models import Cliente, Reparacion


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "rut", "telefono", "correo", "fecha_registro")
    list_filter = ("fecha_registro",)
    search_fields = ("nombre", "rut", "correo")


@admin.register(Reparacion)
class ReparacionAdmin(admin.ModelAdmin):
    list_display = (
        "vehiculo",
        "cliente",
        "costo",
        "fecha_ingreso",
        "terminada",
    )
    list_filter = ("terminada", "fecha_ingreso")
    search_fields = (
        "vehiculo",
        "descripcion",
        "cliente__nombre",
        "cliente__rut",
    )