from rest_framework import viewsets, permissions
from .models import Cita
from .serializers import CitaSerializer

class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all() 
    serializer_class = CitaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Cita.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
