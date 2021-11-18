from rest_framework.response import Response
from serviexpress_api.viewsets.vw_base import BaseViewSet
from serviexpress_api.models import PurchaseOrder, Enterprise, Employee, Provider, PurchaseOrderDetail, Product
from serviexpress_api.serializers.ser_purchase_order import PurchaseOrderSerializer
from django.db import transaction

class PurchaseOrderViewSet(BaseViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def create(self,request):
        with transaction.atomic():
            data = request.data
            errors = self.validate(data)
            if errors:
                return Response(errors, status=400)
            enterprise = Enterprise.objects.get(pk=data['enterprise'])
            employee = Employee.objects.get(pk=data['employee'])
            provider = Provider.objects.get(pk=data['provider'])
            total = data['total']
            description = data['description']
            details = data['details']
            purchase_order = PurchaseOrder(
                enterprise=enterprise,
                employee=employee,
                provider=provider,
                total=total,
                description=description,
                currency=enterprise.currency_default
            )
            purchase_order.save()
            self.save_details(purchase_order,data['details'])

            serializerOrder = PurchaseOrderSerializer(purchase_order)
            return Response(serializerOrder.data)

    def validate(self,data):
        errors = {}
        if len(data['details']) <= 0:
            errors['details'] = 'Debes ingresar al menos un producto'
        return errors
    
    def save_details(self,order,details):
        with transaction.atomic():
            for detail in details:
                product = Product.objects.get(pk=detail['product'])
                purchase_detail = PurchaseOrderDetail(
                    purchase_order=order,
                    product=product,
                    quantity=int(detail['quantity']),
                    total=detail['total']
                )
                purchase_detail.save()