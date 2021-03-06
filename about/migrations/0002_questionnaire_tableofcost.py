# Generated by Django 3.0 on 2021-07-23 08:55

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Qnum', models.PositiveSmallIntegerField(default=1)),
                ('Date', models.DateField(default=datetime.date(2021, 3, 23))),
                ('Date_of_birth', models.DateField(default=datetime.date(2021, 3, 23))),
                ('Age_year', models.PositiveSmallIntegerField(default=3)),
                ('Age_month', models.PositiveSmallIntegerField(default=5)),
                ('LGA', models.CharField(max_length=20)),
                ('Ethnicity', models.CharField(max_length=10)),
                ('Religion', models.CharField(max_length=15)),
                ('Duration_years', models.PositiveSmallIntegerField()),
                ('Duration_months', models.PositiveSmallIntegerField()),
                ('Hospital', models.CharField(max_length=200)),
                ('Family', models.CharField(max_length=50)),
                ('Children', models.PositiveSmallIntegerField()),
                ('Father_education', models.CharField(max_length=50)),
                ('Mother_education', models.CharField(max_length=50)),
                ('Father_occupation', models.CharField(max_length=50)),
                ('Mother_occupation', models.CharField(max_length=50)),
                ('Father_income', models.CharField(max_length=200)),
                ('Mother_income', models.CharField(max_length=200)),
                ('Total_income_per_month', models.PositiveIntegerField()),
                ('Clinic_visits_per_month', models.PositiveIntegerField()),
                ('Visits_to_other_centres', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('Indirect_cost', models.PositiveIntegerField(blank=True, null=True)),
                ('Percentage_of_income_spent', models.PositiveSmallIntegerField()),
                ('Aid_from_other_sources', models.CharField(max_length=3)),
                ('How_much', models.PositiveIntegerField(blank=True, null=True)),
                ('Working', models.CharField(max_length=3)),
                ('Care_taker', models.CharField(blank=True, max_length=200, null=True)),
                ('Cost_of_care_taker', models.PositiveIntegerField(blank=True, null=True)),
                ('Extra_time_spent', models.PositiveSmallIntegerField()),
                ('Stigma', models.CharField(blank=True, max_length=200, null=True)),
                ('Stopped_working', models.CharField(max_length=3)),
                ('Money_foregone', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('Activities_forgone', models.CharField(max_length=3)),
                ('They_are', models.CharField(blank=True, max_length=200, null=True)),
                ('Weight', models.PositiveSmallIntegerField()),
                ('Height', models.PositiveSmallIntegerField()),
                ('Lab_estimation', models.PositiveSmallIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TableOfCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Syringes_Unit_cost', models.IntegerField()),
                ('Syringes_Quantity', models.IntegerField()),
                ('Needles_Unit_cost', models.IntegerField()),
                ('Needles_Quantity', models.IntegerField()),
                ('Glucometer_strips_Unit_cost', models.IntegerField()),
                ('Glucometer_strips_Quantity', models.IntegerField()),
                ('Regular_insulin_Unit_cost', models.IntegerField()),
                ('Regular_insulinQuantity', models.IntegerField()),
                ('Basal_insulin_Unit_cost', models.IntegerField()),
                ('Basal_insulin_Quantity', models.IntegerField()),
                ('Ice_packs_Unit_cost', models.IntegerField()),
                ('Ice_packs_Quantity', models.IntegerField()),
                ('Support_equipment_Unit_cost', models.IntegerField()),
                ('Support_equipment_Quantity', models.IntegerField()),
                ('Cost_of_transportation_Unit_cost', models.IntegerField()),
                ('Cost_of_transportation_Quantity', models.IntegerField()),
                ('Item_9', models.CharField(blank=True, max_length=15, null=True)),
                ('Unit_cost_9', models.IntegerField(blank=True, default=0, null=True)),
                ('Quantity_9', models.IntegerField(blank=True, default=0, null=True)),
                ('Item_10', models.CharField(blank=True, max_length=15, null=True)),
                ('Unit_cost_10', models.IntegerField(blank=True, default=0, null=True)),
                ('Quantity_10', models.IntegerField(blank=True, default=0, null=True)),
                ('question', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='about.Questionnaire')),
            ],
        ),
    ]
