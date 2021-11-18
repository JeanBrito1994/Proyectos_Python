from rest_framework.response import Response
from serviexpress_api.viewsets.vw_base import BaseViewSet
from serviexpress_api.models import DocumentDetail
from serviexpress_api.serializers.ser_document_detail import DocumentDetailSerializer


class DocumentDetailViewSet(BaseViewSet):
    queryset = DocumentDetail.objects.all()
    serializer_class = DocumentDetailSerializer
