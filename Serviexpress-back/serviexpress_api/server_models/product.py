from django.db import models
from .base_model import BaseModel
from .provider import Provider
from .product_category import ProductCategory
from .enterprise import Enterprise


class Product(BaseModel):
    id = models.CharField(primary_key=True, max_length=17)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    expire_date = models.DateField(null=True, blank=True)
    stock = models.IntegerField(default=0)
    critical_stock = models.IntegerField(default=0)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='product', null=True, default=None)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='product', null=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "SE_PRODUCT"
