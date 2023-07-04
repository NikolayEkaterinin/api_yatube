from rest_framework import serializers

from .models import Post, Group, Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault(),
        slug_field='username'
    )
    pub_date = serializers.DateTimeField(read_only=True,
                                         format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Post
        fields = ('id', 'text', 'pub_date', 'author', 'group')


class CommentSerializer(serializers.Serializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault(),
        slug_field='username'
    )
    creator = serializers.DateTimeField(read_only=True,
                                        format='%Y-%m-%d %H:%M:%S'

                                        )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')


class GroupSerializer(serializers.Serializer):


    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')
