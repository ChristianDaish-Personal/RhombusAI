from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'description']

class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField(max_length=None, allow_empty_file=False)