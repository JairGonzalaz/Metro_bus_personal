# Generated by Django 4.2.1 on 2023-05-22 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='nombre',
            field=models.CharField(default='sin nombre', max_length=100),
        ),
    ]
