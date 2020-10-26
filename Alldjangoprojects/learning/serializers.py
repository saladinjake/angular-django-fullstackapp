from rest_framework import serializers
from learning.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id',
                  'title',
                  'description',
                  'published')
