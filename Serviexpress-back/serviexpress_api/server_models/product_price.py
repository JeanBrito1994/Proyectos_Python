from django.db import models
from .base_model import BaseModel
from .currency import Currency
from .product import Product


class ProductPrice(BaseModel):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="prices"
    )
    currency = models.ForeignKey(
        Currency, on_delete=models.CASCADE, related_name="currencies"
    )
    price = models.FloatField(default=0)
    purchase_price = models.FloatField(default=0)

    def __str__(self):
        return "{} {}".format(self.product.name, self.currency.code)

    class Meta:
        db_table = "SE_PRODUCT_PRICE"
