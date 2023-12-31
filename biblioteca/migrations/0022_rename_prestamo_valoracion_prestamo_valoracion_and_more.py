# Generated by Django 4.2.7 on 2023-12-17 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0021_remove_valoracion_valoracion_valoracion_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='valoracion',
            old_name='prestamo',
            new_name='prestamo_valoracion',
        ),
        migrations.RenameField(
            model_name='valoracion',
            old_name='usuario',
            new_name='usuario_valoracion',
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='valoracion_usuario',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='biblioteca.valoracion'),
        ),
    ]
