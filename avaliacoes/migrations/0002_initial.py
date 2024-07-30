# Generated by Django 5.0.6 on 2024-07-29 20:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('avaliacoes', '0001_initial'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='avaliacao',
            name='aluno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avaliacoes_recebidas', to='usuarios.usuario'),
        ),
        migrations.AddField(
            model_name='avaliacao',
            name='profissional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avaliacoes_feitas', to='usuarios.usuario'),
        ),
    ]
