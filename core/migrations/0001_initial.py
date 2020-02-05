# Generated by Django 2.2 on 2020-02-05 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('bairro', models.CharField(max_length=100)),
                ('CEP', models.CharField(max_length=10)),
                ('rua', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=7)),
                ('cpf', models.CharField(blank=True, max_length=20)),
                ('cnpj', models.CharField(blank=True, max_length=30)),
            ],
        ),
    ]
