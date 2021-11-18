from rest_framework.response import Response
from serviexpress_api.viewsets.vw_base import BaseViewSet
from serviexpress_api.models import Client
from serviexpress_api.serializers.ser_client import ClientSerializer


class ClientViewSet(BaseViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
