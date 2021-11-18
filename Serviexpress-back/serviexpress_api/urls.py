from rest_framework.routers import DefaultRouter

from serviexpress_api.views import *
from django.urls import path, include

router = DefaultRouter(trailing_slash=False)
router.register('user/?', UserViewSet)
router.register('client/?', ClientViewSet)
router.register('employee/?', EmployeeViewSet)
router.register('city/?', CityViewSet)
router.register('currency/?', CurrencyViewset)
router.register('enterprise/?', EnterpriseViewSet)
router.register('provider/?', ProviderViewSet)
router.register('purchase_order/?', PurchaseOrderViewSet)
router.register('purchase_order_detail/?', PurchaseOrderDetailViewSet)
router.register('reservation/?', ReservationViewSet)
router.register('document/?', DocumentViewSet)
router.register('document_detail/?', DocumentDetailViewSet)

product_router = DefaultRouter(trailing_slash=False)
product_router.register('',ProductViewSet)
product_router.register('category/?',ProductCategoryViewSet)
product_router.register('price/?',ProductPriceViewSet)

service_router = DefaultRouter(trailing_slash=False)
service_router.register('', ServiceViewSet)
service_router.register('price/?', ServicePriceViewSet)
service_router.register('type/?', ServiceTypeViewSet)

urlpatterns = [
    path(r'auth/login', CustomAuthtoken.as_view()),
    path(r'auth/register', RegisterView.as_view()),
    path('',include(router.urls)),
    path('product/', include(product_router.urls)),
    path('service/',include(service_router.urls))
]
