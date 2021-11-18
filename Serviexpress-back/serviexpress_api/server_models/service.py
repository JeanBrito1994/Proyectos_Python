from django.db import models
from .base_model import BaseModel
from .service_type import ServiceType
from .enterprise import Enterprise

class Service(BaseModel):
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    service_type = models.ForeignKey(ServiceType , on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "SE_SERVICE"