from django.contrib import admin
from .models import SitemaOperativo, Ofimatica, TipoDispositivo, Dispositivo, Nivel, Cargo, Usuario, Encuesta, Unidad
# Register your models here.

admin.site.register(SitemaOperativo)
admin.site.register(Ofimatica)
admin.site.register(TipoDispositivo)
admin.site.register(Dispositivo)
admin.site.register(Cargo)
admin.site.register(Usuario)
admin.site.register(Encuesta)
admin.site.register(Nivel)
admin.site.register(Unidad)