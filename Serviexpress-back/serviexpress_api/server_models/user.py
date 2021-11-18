from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, first_name, last_name, password=None):
        if not username:
            raise ValueError("User must have an username")
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not first_name:
            raise ValueError("User must have a first name")
        if not last_name:
            raise ValueError("User must have a last name")

        user = self.model(email=self.normalize_email(email))
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        user.is_admin = False
        user.is_staff = False
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, first_name, last_name, password=None):
        if not username:
            raise ValueError("User must have an username")
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not first_name:
            raise ValueError("User must have a first name")
        if not last_name:
            raise ValueError("User must have a last name")

        user = self.model(email=self.normalize_email(email))
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_provider = True
        user.save(using=self._db)
        return user

    def create_staffuser(self, username, email, first_name, last_name, password=None):
        if not username:
            raise ValueError("User must have an username")
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not first_name:
            raise ValueError("User must have a first name")
        if not last_name:
            raise ValueError("User must have a last name")

        user = self.model(email=self.normalize_email(email))
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        user.is_admin = False
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    ADMIN = "admin"
    STAFF = "staff"
    PROVIDER = "provider"
    STATUS = [
        (ADMIN, _("Admin User")),
        (STAFF, _("Staff User")),
        (PROVIDER, _("Provider User")),
    ]

    id = models.BigAutoField(primary_key=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    rut = models.CharField(max_length=10, default="")
    email = models.EmailField(_("email address"), unique=True)
    username = models.CharField(max_length=30, unique=True, default="")
    phone = models.CharField(max_length=15, null=False, blank=True, default="")
    first_name = models.CharField(_("first name"), max_length=30)
    last_name = models.CharField(_("last name"), max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_provider = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['password',
                       "email", "first_name", "last_name"]

    objects = CustomUserManager()

    @staticmethod
    def has_perm(perm, obj=None):
        return True
    
    def set_password(self,raw_password):
        self.password = make_password(password=raw_password,salt='serviexpress')

    @staticmethod
    def has_module_perms(app_label):
        return True

    def __str__(self):
        return "{}".format(self.email)

    class Meta:
        db_table = "SE_USER"
