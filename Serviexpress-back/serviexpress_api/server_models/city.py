from django.db import models
from .base_model import BaseModel


class City(BaseModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "SE_CITY"
