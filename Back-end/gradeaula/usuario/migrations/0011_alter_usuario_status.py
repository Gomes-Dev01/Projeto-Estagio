# Generated by Django 4.2.1 on 2023-05-05 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0010_alter_usuario_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='status',
            field=models.CharField(max_length=1),
        ),
    ]
