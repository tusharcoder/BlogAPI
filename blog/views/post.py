from rest_framework.views import APIView
import rest_framework.viewsets as viewsets
from rest_framework.response import Response
import rest_framework.status as status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework.permissions import AllowAny
from django.contrib.auth.hashers import make_password

from blog.serializers import PostSerializer

class PostViewSet(viewsets.mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated,]
    serializer_class = PostSerializer
        