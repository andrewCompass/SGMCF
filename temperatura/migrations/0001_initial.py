# Generated by Django 5.2 on 2025-04-10 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperatura', models.FloatField()),
                ('status', models.CharField(max_length=10)),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
