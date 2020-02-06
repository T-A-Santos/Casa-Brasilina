# Generated by Django 2.2 on 2020-02-06 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200206_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='descricao',
            field=models.CharField(blank=True, choices=[('cel', 'Celular'), ('tel', 'Telefone fixo')], max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='numero',
            field=models.CharField(max_length=7),
        ),
    ]
