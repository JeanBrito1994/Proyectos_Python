from django.db import models
from .base_model import BaseModel
from serviexpress_api.models import Enterprise, Currency, Client, Employee, Service, Product


class Document(BaseModel):
    DOCUMENT_TYPES = [('Boleta', 'boleta'), ('Factura', 'factura')]

    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    services = models.ManyToManyField(Service, db_table='SE_DOCUMENT_SERVICE', blank=True)
    
    total = models.FloatField()
    document_type = models.CharField(max_length=100, choices=DOCUMENT_TYPES)


    def __str__(self):
        return self.id

    class Meta:
        db_table = "SE_DOCUMENT"