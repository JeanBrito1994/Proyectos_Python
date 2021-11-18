
from serviexpress_api.models import User, Client, City
from serviexpress_api.serializers.ser_register import RegisterSerializer
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self,request):
        user = self.serializer_class(data=request.data)
        user.is_valid(raise_exception=True)
        user = user.create(request.data)
        if(request.data.get('create_client', False)):
            client = Client(user=user)
            client.address = request.data.get('address', 'No Especificada')
            city = request.data.get('city', None)
            if city is None: 
                return Response({'city': 'La ciudad es requerida'},status=400)
            if 'id' not in city:
                city = City.objects.filter(name__icontains=city['name'].lower()).first()
                if city is None:
                    city = City(name=city['name'])
                    city.save()
                client.city = city
            else:
                client.city = City.objects.get(pk=city['id'])
            client.save()
        token,_ = Token.objects.get_or_create(user=user)
        #camel case on custom response, not working with camel case parser
        return Response({
            'token': token.key,
            'userId': user.pk,
            'username': user.username,
            'email': user.email,
            'admin': user.is_admin,
            'staff': user.is_staff,
            'provider': user.is_provider
        })
        