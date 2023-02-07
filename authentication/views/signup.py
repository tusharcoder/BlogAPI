from rest_framework.views import APIView
from rest_framework.response import Response
import rest_framework.status as status
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework.permissions import AllowAny
from django.contrib.auth.hashers import make_password

from authentication.serializers import UserSerializer


class RegistrationView(APIView):
    permission_classes = [AllowAny,]

    def post(self, request):
        data = request.data
        email = data.get('email', None)
        password = data.get('password', None)
        first_name = data.get('first_name', None)
        last_name = data.get('last_name', None)
        errors = []
        if email is None:
            errors.append(f'email is required, passed {email}')
        if password is None:
            errors.append(f'password is required, passed {password}')
        if first_name is None:
            errors.append(f'first_name is required, passed {first_name}')
        if last_name is None:
            errors.append(f'last_name is required, passed {last_name}')
        if User.objects.filter(Q(email=email)|Q(username=email)).exists():
            errors.append(f'User already register with provided email, {email}')
        if len(errors)>0:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create(
            username=email,
            email=email,
            password=make_password(password),
            first_name=first_name,
            last_name=last_name,
            is_active=True
            ) # making users activated by default
        data = UserSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)
