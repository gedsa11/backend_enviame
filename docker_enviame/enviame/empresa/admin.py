from django.contrib import admin
from .models import Empresa

# Register your models here.
class EmpresaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


#registrar el servicio y su configuracion
admin.site.register(Empresa, )