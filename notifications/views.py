from rest_framework import viewsets

from .models import Template
from .serializers import TemplateSerializer

class TemplateViewSet(viewsets.ModelViewSet):
    serializer_class = TemplateSerializer

    def get_queryset(self):
        return Template.objects.filter(office_id=1)

    def perform_create(self, serializer):
        serializer.save(office_id=1)
