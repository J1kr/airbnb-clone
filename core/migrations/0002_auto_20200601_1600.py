# Generated by Django 2.2.5 on 2020-06-01 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timestampedmodel',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='timestampedmodel',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
