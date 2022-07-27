from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Follow, Group, Post


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    following = serializers.SlugRelatedField(
        slug_field='username', read_only=True)
    user = serializers.SlugRelatedField(
        slug_field='username', read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Follow
        fields = ('user', 'following')

        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following')
            )
        ]

    def validate_following(self, following):
        if self.context.get('request').user == following:
            raise serializers.ValidationError(
                'На себя подписаться нельзя')
        return following
