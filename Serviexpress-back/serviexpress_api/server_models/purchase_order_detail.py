from django.db import models
from .base_model import BaseModel
from serviexpress_api.models import PurchaseOrder, Product


class PurchaseOrderDetail(BaseModel):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name='details')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total = models.FloatField(default=0)


    def __str__(self):
        return self.id

    class Meta:
        db_table = "SE_PURCHASE_ORDER_DETAIL"