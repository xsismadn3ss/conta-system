from django.contrib import admin
from .models import Jerarquia, Tipo, Cuenta

# Register your models here.
class JerarquiaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre', )
    list_display_links = ('nombre', )

class TipoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre', )
    list_display_links = ('nombre', )



class CuentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'tipo', 'jerarquia', 'estado')
    search_fields = ('nombre', )
    list_display_links = ('nombre', )



admin.site.register(Jerarquia, JerarquiaAdmin)
admin.site.register(Tipo, TipoAdmin)
admin.site.register(Cuenta, CuentaAdmin)