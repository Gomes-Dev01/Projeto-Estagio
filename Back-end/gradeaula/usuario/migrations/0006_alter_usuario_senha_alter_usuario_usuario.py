# Generated by Django 4.2 on 2023-04-21 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("usuario", "0005_alter_usuario_inclusao_alter_usuario_login"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usuario", name="senha", field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="usuario", name="usuario", field=models.CharField(max_length=50),
        ),
    ]