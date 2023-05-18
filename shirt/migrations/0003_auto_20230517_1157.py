# Generated by Django 3.2.18 on 2023-05-17 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shirt', '0002_remove_shirt_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shirt',
            options={'ordering': ['-created_at'], 'verbose_name': 'T-Shirt', 'verbose_name_plural': 'TShirts'},
        ),
        migrations.AlterField(
            model_name='shirt',
            name='color',
            field=models.CharField(choices=[('RED', 'Red'), ('BLUE', 'Blue'), ('GREEN', 'Green')], max_length=50),
        ),
    ]