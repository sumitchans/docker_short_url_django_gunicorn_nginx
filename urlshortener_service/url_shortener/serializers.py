import time

from rest_framework import serializers
from .models import Shortener
from .utils import get_unique_id


class UrlShortenerSerializer(serializers.Serializer):
    long_url = serializers.URLField(required=True)
    short_url = serializers.URLField(read_only=True)

    def create(self, validated_data):
        timestamp = time.time_ns()
        short_id = get_unique_id(timestamp)
        long_url = validated_data["long_url"]
        short = Shortener.objects.create(long_url=long_url, short_url=short_id)
        return short

