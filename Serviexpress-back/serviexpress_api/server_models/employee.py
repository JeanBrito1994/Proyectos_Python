from django.db import models
from .base_model import BaseModel
from .user import User
from .enterprise import Enterprise


class Employee(BaseModel):
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee')
    contract_date = models.DateField(auto_now_add=False, editable=True)
    birth_day = models.DateField(blank=True, editable=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = "SE_EMPLOYEE"
