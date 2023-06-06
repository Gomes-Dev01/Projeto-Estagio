from django.contrib import admin
from .models import Usuario, NivelAcesso, MenuEntrada

admin.site.register(Usuario)
admin.site.register(MenuEntrada)
admin.site.register(NivelAcesso)
#admin.site.register(NivelEntradaMenu)
