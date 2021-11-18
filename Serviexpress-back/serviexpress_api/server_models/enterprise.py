from django.db import models
from .base_model import BaseModel
from serviexpress_api.models import Currency

# Oficina/Sucursal
class Enterprise(BaseModel):
    name = models.CharField(max_length=100)
    currency_default = models.ForeignKey(Currency, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "SE_ENTERPRISE"