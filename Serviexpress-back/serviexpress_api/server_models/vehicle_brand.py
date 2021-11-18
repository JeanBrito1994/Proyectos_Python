from django.db import models
from .base_model import BaseModel


class VehicleBrand(BaseModel):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "SE_VEHICLE_BRAND"
