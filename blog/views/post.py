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
from blog.models import Post

class PostViewSet(viewsets.mixins.CreateModelMixin,
                    viewsets.mixins.ListModelMixin, 
                    viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated,]
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Post.objects.all()
        return queryset
    
    def comments(self, request):
        """
        API to get the comments of the particular post
        """
        pass