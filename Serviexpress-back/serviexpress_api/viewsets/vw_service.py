from rest_framework.response import Response
from serviexpress_api.viewsets.vw_base import BaseViewSet
from serviexpress_api.models import Service, ServicePrice, Enterprise, ServiceType
from serviexpress_api.serializers.ser_service import ServiceSerializer
from rest_framework.exceptions import ValidationError
from django.db import transaction


class ServiceViewSet(BaseViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def create(self, request):
        with transaction.atomic():
            data = request.data
            errors = self.validate(data)
            if errors:
                return Response(errors,status=400)    
            enterprise = Enterprise.objects.get(pk=data['enterprise'])
            service = Service(
                service_type=ServiceType.objects.get(pk=data['service_type']),
                enterprise=enterprise,
                name=data['name'],
                description=data['description']
            )
            service.save()
            price_instance = ServicePrice(
                currency=enterprise.currency_default,
                service=service,
                price=float(data['price'])
            )
            price_instance.save()
            serializedService = ServiceSerializer(service)

            return Response(serializedService.data)
    
    def validate(self,data):
        name = Service.objects.filter(name__icontains=data['name'].lower(),is_active=True, enterprise__pk=data['enterprise']).exists()
        errors = {}
        if name:
            errors['name'] = 'Un Servicio con este nombre ya existe'
        if float(data['price']) <= 0:
            errors['price'] = 'El Precio debe ser mayor a 0' 
        return errors