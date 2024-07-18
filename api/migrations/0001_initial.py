# Generated by Django 5.0.7 on 2024-07-16 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carlist',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('des', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
                ('color', models.CharField(max_length=100)),
            ],
        ),
    ]
