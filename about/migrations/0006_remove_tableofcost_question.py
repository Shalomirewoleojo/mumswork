# Generated by Django 3.0 on 2021-07-23 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_auto_20210723_1451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tableofcost',
            name='question',
        ),
    ]
