# Generated by Django 4.2 on 2023-04-25 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("usuario", "0006_alter_usuario_senha_alter_usuario_usuario"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usuario",
            name="usuario",
            field=models.CharField(max_length=50, unique=True),
        ),
    ]