# Generated by Django 4.2 on 2023-04-18 14:34

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("usuario", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usuario",
            name="senha",
            field=models.CharField(verbose_name=django.contrib.auth.models.User),
        ),
        migrations.AlterField(
            model_name="usuario",
            name="usuario",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
