from rest_framework import serializers
from django.utils import timezone
from .models import Post


class PostSerializer(serializers.Serializer):
    author_id = serializers.IntegerField()
    title = serializers.CharField(max_length=200)
    text = serializers.CharField()
    created_date = serializers.DateTimeField(default=timezone.now)
    published_date = serializers.DateTimeField(default=timezone.now)

    def create(self, validated_data):
        return Post.objects.create(**validated_data)
