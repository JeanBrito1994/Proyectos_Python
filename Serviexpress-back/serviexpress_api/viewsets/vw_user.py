from rest_framework import views
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from serviexpress_api.models import User
from serviexpress_api.serializers.ser_user import UserSerializer
from serviexpress_api.viewsets.vw_base import BaseViewSet


class UserViewSet(BaseViewSet):
    """
    User endpoint
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CustomAuthtoken(ObtainAuthToken):
    def post(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'userId': user.pk,
            'username': user.username,
            'email': user.email,
            'admin': user.is_admin,
            'staff': user.is_staff,
            'provider': user.is_provider
        })
