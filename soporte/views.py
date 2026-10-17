from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated

from .models import Solicitud
from .serializers import SolicitudSerializer
from .permissions import PermisosSolicitud


class SolicitudViewSet(viewsets.ModelViewSet):

    serializer_class = SolicitudSerializer

    permission_classes = [
        IsAuthenticated,
        PermisosSolicitud,
    ]

    def get_queryset(self):
        usuario = self.request.user

        # El administrador puede consultar todas.
        if usuario.is_staff:
            return Solicitud.objects.all()

        # El usuario normal solo consulta las propias.
        return Solicitud.objects.filter(usuario=usuario)

    def perform_create(self, serializer):
        # El propietario se asigna en el servidor.
        serializer.save(usuario=self.request.user)

    def perform_update(self, serializer):
        usuario = self.request.user

        if not usuario.is_staff:
            estado_enviado = (
                'estado' in self.request.data
                and self.request.data.get('estado')
                != serializer.instance.estado
            )

            if estado_enviado:
                raise PermissionDenied(
                    'Solo un administrador puede cambiar el estado.'
                )

        serializer.save()
