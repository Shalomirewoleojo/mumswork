from django import forms
from django.forms import ModelForm, fields, widgets
from django.forms import TextInput, EmailInput, FileInput, Select
from django.contrib.auth.forms import UserCreationForm
from user.models import CustomUser
from .models import *

class ConsentForm(UserCreationForm):
    username = forms.CharField(max_length=30, help_text='username')
    first_name = forms.CharField( help_text='first_name')
    last_name = forms.CharField( help_text='last_name')
    phone_number = forms.DecimalField(required=False, max_digits=11, decimal_places=0, help_text='phone_number')
    ward_name = forms.CharField( help_text='ward_name') 
    assent_name = forms.CharField(required=False,  help_text='assent_name')

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'phone_number', 'ward_name', 'assent_name', 'password1', 'password2')


def save(self, commit=True):
    user = super(ConsentForm, self).save(commit=False)
    if commit:
        user.save()
    return user


class QuestionnaireForm (forms.ModelForm):
    Qnum = models.IntegerField(help_text='qnum',unique=True)
    Date = models.DateField(help_text='date')
    Date_of_birth = models.DateField(help_text='db')
    Age_year= forms.IntegerField(help_text='age', required=False)
    Age_month= forms.IntegerField(help_text='age')
    LGA= forms.CharField( help_text='LGA')
    Ethnicity= forms.CharField( help_text='Ethnicity')
    Religion = forms.CharField( help_text='Religion')
    Duration_years = forms.IntegerField(help_text='yrs')
    Duration_months = forms.IntegerField(help_text='mnth')
    Hospital = forms.CharField(help_text='hosp')
    Family = forms.CharField( help_text='fam')
    Children = forms.IntegerField(help_text='chld')
    Father_education = forms.CharField( help_text='faed')
    Mother_education = forms.CharField( help_text='moed')
    Father_occupation = forms.CharField( help_text='faoc')
    Mother_occupation = forms.CharField( help_text='maoc')
    Father_income = forms.CharField(help_text='fain')
    Mother_income = forms.CharField(help_text='main')
    Total_income_per_month = forms.IntegerField(help_text='tipm')
    Clinic_visits_per_month = forms.IntegerField(help_text='cvpm')
    Visits_to_other_centres = forms.IntegerField(required=False, help_text='visits')

    # Direct_cost = forms.IntegerField(help_text='dc')
    
    # Total_cost = forms.IntegerField(help_text='tc')
    Percentage_of_income_spent = forms.IntegerField(help_text='pi')
    Aid_from_other_sources= forms.CharField(help_text='aid')
    How_much = forms.IntegerField(required=False, help_text='howmuch')
    Working= forms.CharField(help_text='working')
    Care_taker = forms.CharField(required=False, help_text='cata')
    Cost_of_care_taker = forms.IntegerField(required=False, help_text='costcata')
    Extra_time_spent = forms.IntegerField(help_text='extra')
    Stigma = forms.CharField(required=False, help_text='stigma')
    Stopped_working= forms.CharField(help_text='stopwork')
    Money_foregone = forms.IntegerField(required=False, help_text='mofo')
    Activities_forgone= forms.CharField(help_text='acfo')
    They_are = forms.CharField(required=False, help_text='theyare')
    Weight = forms.IntegerField(help_text='weight')
    Height = forms.IntegerField(help_text='height')
    # BMI = forms.IntegerField(help_text='bmi')
    Lab_estimation= forms.IntegerField(help_text='labest')

    class Meta:
        model = Questionnaire
        fields = ( 'Qnum', 'Date', 'Date_of_birth', 'Age_year', 'Age_month', 'LGA', 'Ethnicity', 'Religion', 'Duration_years', 'Duration_months',
        'Hospital', 'Family', 'Children', 'Father_education', 'Mother_education', 'Father_occupation',
        'Mother_occupation', 'Father_income', 'Mother_income', 'Total_income_per_month', 'Clinic_visits_per_month',
        'Visits_to_other_centres', 'Percentage_of_income_spent',
        'Aid_from_other_sources', 'How_much', 'Working', 'Care_taker', 'Cost_of_care_taker', 'Extra_time_spent',
        'Stigma', 'Stopped_working', 'Money_foregone', 'Activities_forgone', 'They_are', 'Weight', 'Height', 'Lab_estimation',
        )

# def save(self, commit=True):
#     user = super(QuestionnaireForm, self).save(commit=False)
#     if commit:
#         user.save()
#     return user


class TableOfCostForm(forms.ModelForm):
    Qnum = models.IntegerField(help_text='qnum',unique=True)
    #all this isn't necessary
    Syringes_Unit_cost = forms.IntegerField()
    Syringes_Quantity = forms.IntegerField()
    # Syringes_Cost_per_month = forms.IntegerField()

    Needles_Unit_cost = forms.IntegerField()
    Needles_Quantity = forms.IntegerField()
    # Needles_Cost_per_month = forms.IntegerField()

    Glucometer_strips_Unit_cost = forms.IntegerField()
    Glucometer_strips_Quantity = forms.IntegerField()
    # Glucometer_strips_Cost_per_month = forms.IntegerField()

    Regular_insulin_Unit_cost = forms.IntegerField()
    Regular_insulinQuantity = forms.IntegerField()
    # Regular_insulin_Cost_per_month = forms.IntegerField()

    Basal_insulin_Unit_cost = forms.IntegerField()
    Basal_insulin_Quantity = forms.IntegerField()
    # Basal_insulin_Cost_per_month = forms.IntegerField()

    Ice_packs_Unit_cost = forms.IntegerField()
    Ice_packs_Quantity = forms.IntegerField()
    # Ice_packs_Cost_per_month = forms.IntegerField()

    Support_equipment_Unit_cost = forms.IntegerField()
    Support_equipment_Quantity = forms.IntegerField()
    # Support_equipment_Cost_per_month = forms.IntegerField()

    Cost_of_transportation_Unit_cost = forms.IntegerField()
    Cost_of_transportation_Quantity = forms.IntegerField()
    # Cost_of_transportation_Cost_per_month = forms.IntegerField()

    Item_9 = forms.CharField(required=False)
    Unit_cost_9 = forms.IntegerField(required=False)
    Quantity_9 = forms.IntegerField(required=False)
    Cost_per_month_9 = forms.IntegerField(required=False)

    Item_10 = forms.CharField(required=False)
    Unit_cost_10 = forms.IntegerField(required=False)
    Quantity_10 = forms.IntegerField(required=False)
    Cost_per_month_10 = forms.IntegerField(required=False)

    Indirect_cost = forms.IntegerField(required=False, help_text='ic')

    class Meta:
        model = TableOfCost
        fields = ('Qnum', 'Syringes_Unit_cost','Syringes_Quantity', 'Needles_Unit_cost',
        'Needles_Quantity', 'Glucometer_strips_Unit_cost', 'Glucometer_strips_Quantity',
        'Regular_insulin_Unit_cost', 'Regular_insulinQuantity',
        'Basal_insulin_Unit_cost', 'Basal_insulin_Quantity', 'Ice_packs_Unit_cost',
        'Ice_packs_Quantity', 'Support_equipment_Unit_cost', 'Support_equipment_Quantity',
        'Cost_of_transportation_Unit_cost','Cost_of_transportation_Quantity',
        'Item_9', 'Unit_cost_9', 'Quantity_9', 'Cost_per_month_9', 'Item_10', 'Unit_cost_10', 'Quantity_10', 'Cost_per_month_10',
        'Indirect_cost',
        )

        # use fields = '__all__' next time

# def save(self, commit=True):
#     user = super(TableOfCostForm, self).save(commit=False)
#     if commit:
#         user.save()
#     return user