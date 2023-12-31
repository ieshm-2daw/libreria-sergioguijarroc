# Generated by Django 4.2.7 on 2023-12-13 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0004_alter_libro_valoracion_media'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='numero_valoraciones',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='libro',
            name='disponibilidad',
            field=models.CharField(choices=[('D', 'Disponible'), ('P', 'Prestado'), ('E', 'En proceso de préstamo')], default='D', max_length=1),
        ),
        migrations.AlterField(
            model_name='libro',
            name='valoracion_media',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
