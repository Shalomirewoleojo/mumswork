# Generated by Django 3.0 on 2021-07-23 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_auto_20210723_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaire',
            name='Age_year',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tableofcost',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.Questionnaire'),
        ),
    ]
