# Generated by Django 3.2.18 on 2023-05-19 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shirt', '0013_alter_shirt_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shirt',
            name='name',
            field=models.CharField(default='proof', max_length=20),
        ),
    ]