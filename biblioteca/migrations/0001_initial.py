# Generated by Django 4.2.7 on 2023-11-29 08:50

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('dni', models.CharField(blank=True, max_length=9, null=True, unique=True)),
                ('direccion', models.CharField(blank=True, max_length=200, null=True)),
                ('telefono', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(9)])),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('biogafia', models.TextField()),
                ('foto', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('direccion', models.TextField()),
                ('sitio_web', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=13)),
                ('titulo', models.CharField(max_length=50)),
                ('fecha_publicacion', models.DateField()),
                ('genero', models.CharField(max_length=20)),
                ('resumen', models.TextField()),
                ('disponibilidad', models.CharField(choices=[('D', 'Disponible'), ('P', 'Prestado'), ('E', 'En proceso de préstamo')], max_length=20)),
                ('portada', models.ImageField(blank=True, null=True, upload_to='portadas/')),
                ('Editorial', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='biblioteca.editorial')),
                ('autor', models.ManyToManyField(blank=True, to='biblioteca.autor')),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_prestamo', models.DateField()),
                ('fecha_devolucion', models.DateField()),
                ('estado_prestamo', models.CharField(choices=[('D', 'Disponible'), ('P', 'Prestado')], max_length=1)),
                ('Usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('libro_prestado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.libro')),
            ],
        ),
        migrations.AddField(
            model_name='editorial',
            name='Libros',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='biblioteca.libro'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='Prestamo',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='biblioteca.prestamo'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]