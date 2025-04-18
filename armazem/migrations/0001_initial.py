# Generated by Django 5.2 on 2025-04-05 22:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('preco', models.DecimalField(decimal_places=2, default=0.0, help_text='Preço por Kg', max_digits=10, verbose_name='Preço em (R$)')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='armazem.categoria')),
            ],
        ),
    ]
