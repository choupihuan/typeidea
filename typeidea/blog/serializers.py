from rest_framework import serializers

from .models import Post


class PostSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title','category','desc','content_html','create_time']