# Generated by Django 3.2.18 on 2023-05-17 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shirt', '0008_alter_shirt_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shirt',
            name='color',
            field=models.CharField(choices=[('R', 'Rojo'), ('A', 'Azul'), ('Am', 'Amarillo'), ('N', 'Negro'), ('B', 'Marron'), ('BL', 'Blanco')], max_length=50),
        ),
    ]
