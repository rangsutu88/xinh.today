from rest_framework import serializers
from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = (
            'id', 'source', 'url', 'point', 'posted_date', 'created_at'
        )
