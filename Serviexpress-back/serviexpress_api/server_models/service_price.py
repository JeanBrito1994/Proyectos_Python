from django.db import models
from .base_model import BaseModel
from .currency import Currency
from .service import Service


class ServicePrice(BaseModel):
    price = models.FloatField(default=0)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='prices')

    def __str__(self):
        return "{} {}{}".format(self.service.name, self.currency.code, self.price)

    class Meta:
        db_table = "SE_SERVICE_PRICE"