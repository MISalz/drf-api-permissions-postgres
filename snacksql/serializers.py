from rest_framework import serializers
from .models import SnackSQL


class SnacksSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ("id", "owner","name", "description", "created_at")
    model = SnackSQL