# Generated by Django 5.0.6 on 2024-07-30 08:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('exercicios', '0001_initial'),
        ('treinos', '0002_alter_treino_aluno_alter_treino_personal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Execucao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serie', models.PositiveIntegerField()),
                ('repeticoes', models.PositiveIntegerField()),
                ('carga', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('status', models.BooleanField(default=False)),
                ('exercicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='execucoes', to='exercicios.exercicio')),
                ('treino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='execucoes', to='treinos.treino')),
            ],
        ),
    ]
