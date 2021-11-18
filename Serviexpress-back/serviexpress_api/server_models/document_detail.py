from django.db import models
from .base_model import BaseModel
from serviexpress_api.models import Product, Document


class DocumentDetail(BaseModel):
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='details')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total = models.FloatField(default=0)


    def __str__(self):
        return self.id

    class Meta:
        db_table = "SE_DOCUMENT_DETAIL"