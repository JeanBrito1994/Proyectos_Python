from django.db import models
from .base_model import BaseModel
from .enterprise import Enterprise

class Provider(BaseModel):
    name = models.CharField(max_length=20)
    contact_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    field = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "SE_PROVIDER"
