# Generated by Django 4.2.7 on 2023-12-16 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0018_remove_libro_numero_valoraciones_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='valoracion_media',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
