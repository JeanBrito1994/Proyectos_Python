from django.db import models


class BaseModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    is_active = models.BooleanField(default=True)

    @classmethod
    def hasField(self, field):
        try:
            self._meta.get_field(field)
            return True
        except Exception:
            return False
    class Meta:
        abstract = True
