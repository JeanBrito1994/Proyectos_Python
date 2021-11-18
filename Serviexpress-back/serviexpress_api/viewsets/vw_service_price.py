from rest_framework.response import Response
from serviexpress_api.viewsets.vw_base import BaseViewSet
from serviexpress_api.models import ServicePrice
from serviexpress_api.serializers.ser_service_price import ServicePriceSerializer


class ServicePriceViewSet(BaseViewSet):
    queryset = ServicePrice.objects.all()
    serializer_class = ServicePriceSerializer
