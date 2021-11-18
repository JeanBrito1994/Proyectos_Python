from rest_framework.response import Response
from serviexpress_api.viewsets.vw_base import BaseViewSet
from serviexpress_api.models import Provider
from serviexpress_api.serializers.ser_provider import ProviderSerializer


class ProviderViewSet(BaseViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
