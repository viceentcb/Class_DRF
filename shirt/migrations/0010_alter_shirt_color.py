# Generated by Django 3.2.18 on 2023-05-18 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shirt', '0009_alter_shirt_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shirt',
            name='color',
            field=models.CharField(choices=[('R', 'Rojo'), ('A', 'Azul'), ('Am', 'Amarillo'), ('N', 'Negro'), ('M', 'Marron'), ('B', 'Blanco')], max_length=50),
        ),
    ]
