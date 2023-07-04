from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied

from rest_framework import viewsets, generics
from rest_framework import status

from posts.models import (Post,
                          Group,
                          Comment
                          )
from posts.serializers import (PostSerializer,
                               CommentSerializer,
                               GroupSerializer
                               )
from rest_framework.response import Response


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super(PostViewSet, self).perform_update(serializer)

    def post_delete_not_author(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        if request.method == 'DELETE':
            user = request.user
            if user != post.author:
                return Response(status=status.HTTP_403_FORBIDDEN)
            return Response(status=status.HTTP_204_NO_CONTENT)


class GroupList(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupDetails(generics.RetrieveAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentEdit(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
