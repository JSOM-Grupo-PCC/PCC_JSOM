# Generated by Django 4.2.7 on 2024-06-09 21:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('programas', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exercicios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='programa',
            name='aluno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='programas_inscritos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='programa',
            name='exercicios',
            field=models.ManyToManyField(to='exercicios.exercicio'),
        ),
        migrations.AddField(
            model_name='programa',
            name='personal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='programas_criados', to=settings.AUTH_USER_MODEL),
        ),
    ]
