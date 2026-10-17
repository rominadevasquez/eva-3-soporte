from django.contrib import admin
from .models import Solicitud


@admin.register(Solicitud)
class SolicitudAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'titulo',
        'categoria',
        'estado',
        'usuario',
        'fecha_creacion',
    )

    list_filter = ('categoria', 'estado')

    search_fields = ('titulo', 'descripcion')
