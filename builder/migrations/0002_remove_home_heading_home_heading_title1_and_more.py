# Generated by Django 4.1.3 on 2022-11-08 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='heading',
        ),
        migrations.AddField(
            model_name='home',
            name='heading_title1',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='home',
            name='heading_title2',
            field=models.TextField(blank=True, max_length=150),
        ),
    ]
