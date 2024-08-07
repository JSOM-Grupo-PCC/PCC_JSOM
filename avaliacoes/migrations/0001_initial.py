# Generated by Django 5.0.6 on 2024-07-29 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso', models.DecimalField(decimal_places=2, max_digits=5)),
                ('altura', models.DecimalField(decimal_places=2, max_digits=5)),
                ('observacao', models.TextField(blank=True, null=True)),
                ('data_avaliacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
