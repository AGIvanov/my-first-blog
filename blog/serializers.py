from rest_framework import serializers
from django.utils import timezone
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueTogetherValidator
from .models import Post

class PostSerializer(serializers.Serializer):
    author = serializers.CharField(source='author.username', max_length=200)
    title = serializers.CharField(max_length=200)
    text = serializers.CharField()
    created_date = serializers.DateTimeField(default=timezone.now)
    published_date = serializers.DateTimeField(default=timezone.now)

    class Meta:
        validators = [
            UniqueTogetherValidator(
                queryset=Post.objects,
                fields=['title', 'text', 'created_date', 'published_date']
            )
        ]


    def create(self, validated_data):
        return Post.objects.create(**validated_data)