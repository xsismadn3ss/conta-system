from django.contrib import admin
from .models import Tipo, LibroMayor

# Register your models here.
class TipoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre', )
    list_per_page = 50

class LibroMayorAdmin(admin.ModelAdmin):
    list_display = ('id', 'cuenta', 'saldo_anterior', 'saldo_anterior', 'movimiento', 'tipo_movimiento')
    list_display_links = ('cuenta', )
    list_per_page = 50

admin.site.register(Tipo, TipoAdmin)
admin.site.register(LibroMayor, LibroMayorAdmin)
