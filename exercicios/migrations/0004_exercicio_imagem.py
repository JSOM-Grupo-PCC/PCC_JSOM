# Generated by Django 4.2.7 on 2024-07-05 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercicios', '0003_alter_exercicio_grupo_alter_exercicio_nome_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercicio',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='exercicios/'),
        ),
    ]
