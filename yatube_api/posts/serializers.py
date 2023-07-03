from rest_framework import serializers

from .models import Post, Group, Comment


class PostSerializer(serializers.Serializer):
    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.Serializer):
    class Meta:
        model = Comment
        fields = '__all__'


class GroupSerializer(serializers.Serializer):
    class Meta:
        model = Group
        fields = '__all__'
