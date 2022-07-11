from django.contrib import admin
from .models import Dispositivo, Lecturas, Statusdispositivo, Tiposdispositivo

# Register your models here.
# Registramos los nombres de las tablas
admin.site.register(Dispositivo)
admin.site.register(Lecturas)
admin.site.register(Statusdispositivo)
admin.site.register(Tiposdispositivo)