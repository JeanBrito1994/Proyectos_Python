from rest_framework.response import Response
from serviexpress_api.viewsets.vw_base import BaseViewSet
from serviexpress_api.models import PurchaseOrderDetail
from serviexpress_api.serializers.ser_purchase_order_detail import PurchaseOrderDetailSerializer


class PurchaseOrderDetailViewSet(BaseViewSet):
    queryset = PurchaseOrderDetail.objects.all()
    serializer_class = PurchaseOrderDetailSerializer
