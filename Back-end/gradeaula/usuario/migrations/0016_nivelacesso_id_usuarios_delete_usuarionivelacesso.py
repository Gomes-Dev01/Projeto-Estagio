# Generated by Django 4.2 on 2023-05-17 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("usuario", "0015_remove_usuarionivelacesso_id_usuario_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="nivelacesso",
            name="id_usuarios",
            field=models.ManyToManyField(to="usuario.usuario"),
        ),
        migrations.DeleteModel(name="usuarioNivelAcesso",),
    ]
