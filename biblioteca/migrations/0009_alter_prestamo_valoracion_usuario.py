# Generated by Django 4.2.7 on 2023-12-14 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0008_alter_prestamo_valoracion_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='valoracion_usuario',
            field=models.IntegerField(default=0),
        ),
    ]
