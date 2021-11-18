# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Administrador(models.Model):
    id_admin = models.FloatField(primary_key=True)
    nombre_admin = models.CharField(max_length=30)
    apellido_admin = models.CharField(max_length=30)
    contrasena = models.CharField(max_length=30)
    correo = models.CharField(max_length=50)
    tipousuario_admin = models.ForeignKey('Tipousuario', models.DO_NOTHING, db_column='tipousuario_admin')

    def __str__(self):
        return self.nombre_admin

    class Meta:
        managed = False
        db_table = 'administrador'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Banco(models.Model):
    id_banco = models.FloatField(primary_key=True)
    nombre_banco = models.CharField(max_length=40)


    def __str__(self):
        return self.nombre_banco

    class Meta:
        managed = False
        db_table = 'banco'


class Comuna(models.Model):
    id_comuna = models.FloatField(primary_key=True)
    nombre_comuna = models.CharField(max_length=20)


    def __str__(self):
        return self.nombre_comuna

    class Meta:
        managed = False
        db_table = 'comuna'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Funcionario(models.Model):
    id_funcionario = models.FloatField(primary_key=True)
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=40)
    correo = models.CharField(max_length=40)
    cargo_funcionario = models.CharField(max_length=40, blank=True, null=True)
    tipousuario_fun = models.ForeignKey('Tipousuario', models.DO_NOTHING, db_column='tipousuario_fun')


    def __str__(self):
        return self.nombres, self.apellidos

    class Meta:
        managed = False
        db_table = 'funcionario'


class Tipousuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    tipo_usuario = models.CharField(max_length=20, blank=True, null=False)

    def __str__(self):
        return self.tipo_usuario

    class Meta:
        managed = False
        db_table = 'tipousuario'


class Usuario(models.Model):
    rut = models.FloatField(primary_key=True)
    rut_dv = models.CharField(max_length=1)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    direccion = models.CharField(max_length=40)
    comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='comuna', blank=True, null=False)
    correo = models.CharField(max_length=40)
    tarjeta_credito = models.BigIntegerField()
    mes_expiracion = models.IntegerField()
    anio_expiracion = models.IntegerField()
    banco = models.ForeignKey(Banco, models.DO_NOTHING, db_column='banco', blank=True, null=False)
    contrasena = models.CharField(max_length=20)
    tipousuario = models.ForeignKey(Tipousuario, models.DO_NOTHING, db_column='tipousuario', blank=True, null=False)
    estado = models.CharField(max_length=1, blank=True, null=False)

    def __str__(self):
        return self.nombre, self.apellido, self(tipousuario)

    class Meta:
        managed = False
        db_table = 'usuario'

