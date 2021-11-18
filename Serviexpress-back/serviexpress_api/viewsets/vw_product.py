from rest_framework.response import Response
from serviexpress_api.viewsets.vw_base import BaseViewSet
from serviexpress_api.models import Product, Enterprise,ProductCategory, Provider, ProductPrice
from serviexpress_api.serializers.ser_product import ProductSerializer
from django.db import transaction
from django.utils.crypto import get_random_string

class ProductViewSet(BaseViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        provider = self.request.query_params.get('provider', None)
        if provider is not None:
            queryset = queryset.filter(provider__pk=provider)
        return queryset


    def create(self,request):
        with transaction.atomic():
            data = request.data
            errors = self.validate(data)
            if errors:
                return Response(errors, status=400)
            enterprise = Enterprise.objects.get(pk=data['enterprise'])
            category = ProductCategory.objects.get(pk=data['category'])
            provider = Provider.objects.get(pk=data['provider'])
            generated_id = self.generate_id(data)
            product = Product(
                id=generated_id,
                enterprise=enterprise,
                name=data['name'],
                description=data['description'],
                expire_date=data['expire_date'],
                stock=data['stock'],
                critical_stock=data['critical_stock'],
                provider=provider,
                category=category,
            )
            product.save()
            price_instance = ProductPrice(
                currency=enterprise.currency_default,
                product=product,
                price=data['price'],
                purchase_price=data['purchase_price'],
            )
            price_instance.save()
            serializedProduct = ProductSerializer(product)
            return Response(serializedProduct.data)

    def validate(self,data):
        name = Product.objects.filter(name__icontains=data['name'], enterprise__pk=data['enterprise'], is_active=True).exists()
        errors = {}
        if name:
            errors['name'] = 'Un Producto con este nombre ya existe'
        if float(data['price']) <= 0:
            errors['price'] = 'El Precio debe ser mayor a 0' 
        if float(data['purchase_price']) <= 0:
            errors['purchase_price'] = 'El Precio de Compra debe ser mayor a 0' 
        return errors

    def generate_id(self,data):
        provider = '{:03d}'.format(int(str(data['provider'])[:3]))
        category = '{:03d}'.format(int(str(data['category'])[:3]))
        expire_date = '00000000'
        if data['expire_date']:
            expire_date = str(data['expire_date']).replace('-', '')

        return '{}{}{}{}'.format(provider,category,expire_date, get_random_string(length=3, allowed_chars='0123456789'))
