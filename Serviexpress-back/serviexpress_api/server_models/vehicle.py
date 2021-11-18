from django.db import models
from .vehicle_brand import VehicleBrand
from .vehicle_type import VehicleType
from .enterprise import Enterprise
from .client import Client


class Vehicle(models.Model):
    patent = models.IntegerField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    color = models.CharField(max_length=20, default="")
    motor = models.CharField(max_length=20, default="")
    year = models.PositiveSmallIntegerField()
    brand = models.ForeignKey(
        VehicleBrand, on_delete=models.CASCADE, related_name="brands"
    )
    type_v = models.ForeignKey(
        VehicleType, on_delete=models.CASCADE, related_name="types"
    )

    def __str__(self):
        return str(self.patent)

    class Meta:
        db_table = "SE_VEHICLE"
