from django.db import models
from .base_model import BaseModel
from serviexpress_api.models import Enterprise, Employee, Product, Provider,Currency


class PurchaseOrder(BaseModel):
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    total = models.FloatField()
    description = models.TextField(blank=True, default="")
    
    def __str__(self):
        return self.id

    class Meta:
        db_table = "SE_PURCHASE_ORDER"