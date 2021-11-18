from django.db import models
from .base_model import BaseModel
from .enterprise import Enterprise

class ProductCategory(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "SE_PRODUCT_CATEGORY"
