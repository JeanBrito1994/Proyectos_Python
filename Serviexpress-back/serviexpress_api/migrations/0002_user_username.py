# Generated by Django 3.2 on 2021-05-02 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviexpress_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=30, unique=True),
        ),
    ]