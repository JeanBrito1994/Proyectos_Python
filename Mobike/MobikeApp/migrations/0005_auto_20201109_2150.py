# Generated by Django 3.1.3 on 2020-11-10 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MobikeApp', '0004_auto_20201109_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='rut',
            field=models.CharField(max_length=12, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='tarjeta_credito',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='tipousuario',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterModelTable(
            name='usuario',
            table=None,
        ),
    ]
