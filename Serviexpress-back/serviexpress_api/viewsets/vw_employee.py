from rest_framework.response import Response
from serviexpress_api.viewsets.vw_base import BaseViewSet
from serviexpress_api.models import Employee
from serviexpress_api.serializers.ser_employee import EmployeeSerializer


class EmployeeViewSet(BaseViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.query_params.get('user', None)
        if user is not None:
            queryset = queryset.filter(user__pk=user)
        return queryset