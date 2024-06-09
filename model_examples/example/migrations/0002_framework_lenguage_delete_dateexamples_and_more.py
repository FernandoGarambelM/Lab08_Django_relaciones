# Generated by Django 5.0.6 on 2024-06-09 03:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Framework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Lenguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='DateExamples',
        ),
        migrations.DeleteModel(
            name='nullExample',
        ),
        migrations.DeleteModel(
            name='Simple',
        ),
        migrations.AddField(
            model_name='framework',
            name='lenguage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='example.lenguage'),
        ),
    ]
