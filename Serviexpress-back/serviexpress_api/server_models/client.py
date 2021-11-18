from django.db import models
from .base_model import BaseModel
from .city import City
from .user import User


class Client(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client')
    address = models.TextField()
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, related_name="comuna")
    is_trusted = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username

    class Meta:
        db_table = "SE_CLIENT"
