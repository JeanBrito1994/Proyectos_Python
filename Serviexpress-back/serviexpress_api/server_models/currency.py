from django.db import models
from .base_model import BaseModel


class Currency(BaseModel):
    name = models.CharField(max_length=100, default="")
    code = models.CharField(max_length=10, default="")
    symbol = models.CharField(max_length=10, default="$", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "SE_CURRENCY"
