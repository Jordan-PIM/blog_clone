from rest_framework import serializers

from .models import Post, Comment


class PostSerializer(serializers.HyperlinkedModelSerializer):
    created_date = serializers.DateTimeField(format='%d-%m-%y')
    number = serializers.IntegerField(default=100)
    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
