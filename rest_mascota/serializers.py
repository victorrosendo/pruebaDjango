from django.db.models.base import Model
from rest_framework import serializers
from core.models import Raza

class RazaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raza
        fields = ['codigo','nombreRaza']


