from rest_framework.response import Response
from serviexpress_api.viewsets.vw_base import BaseViewSet
from serviexpress_api.models import ProductPrice
from serviexpress_api.serializers.ser_product_price import ProductPriceSerializer


class ProductPriceViewSet(BaseViewSet):
    queryset = ProductPrice.objects.all()
    serializer_class = ProductPriceSerializer
