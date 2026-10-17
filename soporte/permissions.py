from rest_framework.permissions import BasePermission


class PermisosSolicitud(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):

        # El administrador puede acceder a cualquier solicitud.
        if request.user.is_staff:
            return True

        # Los usuarios normales no pueden eliminar.
        if request.method == 'DELETE':
            return False

        # El usuario normal solo puede acceder a sus solicitudes.
        return obj.usuario_id == request.user.id
    