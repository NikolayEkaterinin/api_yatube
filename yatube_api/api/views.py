from rest_framework import viewsets

from posts.models import Post, Group, Comment
from posts.serializers import PostSerializer, CommentSerializer, GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer