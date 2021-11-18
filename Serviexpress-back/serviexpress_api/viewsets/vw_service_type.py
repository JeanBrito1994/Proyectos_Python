from rest_framework.response import Response
from serviexpress_api.viewsets.vw_base import BaseViewSet
from serviexpress_api.models import ServiceType
from serviexpress_api.serializers.ser_service_type import ServiceTypeSerializer


class ServiceTypeViewSet(BaseViewSet):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer
