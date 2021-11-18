from rest_framework.response import Response
from serviexpress_api.viewsets.vw_base import BaseViewSet
from serviexpress_api.models import Reservation, Client
from serviexpress_api.serializers.ser_reservation import ReservationSerializer
from rest_framework.exceptions import ValidationError
from django.db import transaction


class ReservationViewSet(BaseViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.query_params.get('user', None)
        if user is not None:
            queryset = queryset.filter(client__user__pk=user)   
        return queryset
    

    def create(self,request):
        with transaction.atomic():
            data = request.data
            if Reservation.objects.filter(
                is_active=True,
                enterprise__pk=data['enterprise'],
                reservation_date=data['reservation_date'],                
            ).exists():
                return Response(dict(detail='Esta Hora ya está ocupada'),status=400)
            
            reservation = Reservation(
                client = Client.objects.get(user__pk=data['user']),
                enterprise_id = data['enterprise'],
                reservation_date= data['reservation_date'],                
            )
            reservation.save()
            reservation.services.set(data['services'])
            resSerializer = ReservationSerializer(reservation, many=False)
            return Response(resSerializer.data)
