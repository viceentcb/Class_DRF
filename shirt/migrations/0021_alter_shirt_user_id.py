# Generated by Django 3.2.18 on 2023-06-14 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shirt', '0020_alter_shirt_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shirt',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
