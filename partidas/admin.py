from django.contrib import admin
from .models import PartidaRegistro, Detalles

# Register your models here.
class RegistroAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'fecha_creacion', 'descripcion')
    search_fields = ('titulo', 'descripcion')
    readonly_fields = ('fecha_creacion',)
    list_per_page = 50

class DetallesAdmin(admin.ModelAdmin):
    list_display = ('id', 'partida', 'catalogo_cuentas','monto_debe', 'monto_haber')
    list_display_links = ('catalogo_cuentas', 'partida')
    list_per_page = 50

admin.site.register(PartidaRegistro, RegistroAdmin)
admin.site.register(Detalles, DetallesAdmin)