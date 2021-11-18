from rest_framework.response import Response
from serviexpress_api.viewsets.vw_base import BaseViewSet
from serviexpress_api.models import City
from serviexpress_api.serializers.ser_city import CitySerializer
from rest_framework.exceptions import ValidationError
from django.db import transaction


class CityViewSet(BaseViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def create(self, request):
        with transaction.atomic():
            name = request.data.get('name', None)
            if name is None:
                return ValidationError(detail='Name is required')
            if City.objects.filter(name__icontains=name.lower()).exists():
                return Response(dict(name='Una Ciudad con este nombre ya existe'),status=400)
            
            city = City(
                name=name
            )
            city.save()
            serializer = self.serializer_class(city)
            return Response(serializer.data)