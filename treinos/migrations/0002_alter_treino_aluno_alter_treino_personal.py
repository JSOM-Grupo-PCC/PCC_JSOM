# Generated by Django 5.0.6 on 2024-07-29 20:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treinos', '0001_initial'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treino',
            name='aluno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='treinos_como_aluno', to='usuarios.usuario'),
        ),
        migrations.AlterField(
            model_name='treino',
            name='personal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='treinos_como_personal', to='usuarios.usuario'),
        ),
    ]
