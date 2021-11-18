from rest_framework.response import Response
from serviexpress_api.viewsets.vw_base import BaseViewSet
from serviexpress_api.models import Currency
from serviexpress_api.serializers.ser_currency import CurrencySerializer


class CurrencyViewset(BaseViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
