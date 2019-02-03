from rest_framework import serializers

from .models import Template, Office


class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = ('id', 'name', 'sms', 'email',)
