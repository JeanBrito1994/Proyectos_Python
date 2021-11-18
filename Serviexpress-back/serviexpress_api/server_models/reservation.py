from django.db import models
from .base_model import BaseModel
from .client import Client
from .service import Service
from .enterprise import Enterprise


class Reservation(BaseModel):

    STATUS = [('reserved','Reservado'), ('completed', 'Completado'), ('canceled', 'Cancelado')]

    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    reservation_date = models.DateTimeField(auto_now=False)
    note = models.CharField(max_length=200, blank=True, default='')
    services = models.ManyToManyField(Service, db_table='SE_RESERVATION_SERVICE')
    status = models.CharField(max_length=100, choices=STATUS, default='reserved')


    class Meta:
        db_table = "SE_RESERVATION"