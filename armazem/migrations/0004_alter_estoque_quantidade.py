# Generated by Django 5.2 on 2025-04-05 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armazem', '0003_estoque_quantidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estoque',
            name='quantidade',
            field=models.DecimalField(decimal_places=3, default=0.0, help_text='Quantidade em Kg', max_digits=10, verbose_name='Quantidade em (Kg)'),
        ),
    ]
