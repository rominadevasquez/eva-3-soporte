from rest_framework import serializers
from .models import Solicitud


class SolicitudSerializer(serializers.ModelSerializer):

    class Meta:
        model = Solicitud

        fields = [
            'id',
            'titulo',
            'descripcion',
            'categoria',
            'estado',
            'fecha_creacion',
            'usuario',
        ]

        read_only_fields = [
            'id',
            'fecha_creacion',
            'usuario',
        ]

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get('request')

        if request and request.user.is_authenticated:
            if not request.user.is_staff:
                fields['estado'].read_only = True

        return fields
