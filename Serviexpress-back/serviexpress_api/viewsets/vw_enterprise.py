from rest_framework.response import Response
from serviexpress_api.viewsets.vw_base import BaseViewSet
from serviexpress_api.models import Enterprise
from serviexpress_api.serializers.ser_enterprise import EnterpriseSerializer


class EnterpriseViewSet(BaseViewSet):
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializer
