# Generated by Django 4.1.7 on 2023-03-25 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('usuario', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'usuario',
            },
        ),
        migrations.CreateModel(
            name='ventas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('detalle', models.CharField(max_length=100)),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inicioApp.usuario')),
            ],
            options={
                'db_table': 'ventas',
            },
        ),
        migrations.CreateModel(
            name='compras',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('detalle', models.CharField(max_length=100)),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inicioApp.usuario')),
            ],
            options={
                'db_table': 'compras',
            },
        ),
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ci', models.IntegerField(verbose_name=10)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('telefono', models.IntegerField(verbose_name=10)),
                ('email', models.EmailField(max_length=100)),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inicioApp.usuario')),
            ],
            options={
                'db_table': 'clientes',
            },
        ),
    ]
