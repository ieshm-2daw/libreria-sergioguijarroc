# Generated by Django 4.2.7 on 2023-12-12 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='prestamo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prestamos_usuario', to='biblioteca.prestamo'),
        ),
    ]
