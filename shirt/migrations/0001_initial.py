# Generated by Django 3.2.18 on 2023-05-09 15:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shirt',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('color', models.CharField(max_length=50)),
                ('stock', models.IntegerField()),
                ('phrase', models.CharField(max_length=100)),
                ('emoji', models.CharField(max_length=10)),
                ('photo', models.ImageField(upload_to='shirts/')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'T-Shirt',
                'verbose_name_plural': 'TShirts',
            },
        ),
    ]
