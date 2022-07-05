from rest_framework import serializers
from django.utils import timezone

class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    text = serializers.CharField()
    published_date = serializers.DateTimeField(default=timezone.now)
    author = serializers.CharField(source='author.username', max_length=200)