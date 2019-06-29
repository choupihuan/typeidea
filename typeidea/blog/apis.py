from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import Post
from .serializers import PostSerialiazer


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostSerialiazer
    queryset = Post.objects.filter(status=Post.STATUS_NORMAL)

