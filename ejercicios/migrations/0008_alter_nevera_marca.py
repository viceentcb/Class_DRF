# Generated by Django 3.2.18 on 2023-06-07 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ejercicios', '0007_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nevera',
            name='marca',
            field=models.CharField(blank=True, default='Bosh', max_length=100, null=True),
        ),
    ]
