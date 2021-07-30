from django.contrib import admin
from .models import *
# Register your models here.

class MediaAdmin (admin.ModelAdmin):
    list_display= ['id']

class UserProfileAdmin (admin.ModelAdmin):
    list_display= ['first_name', 'last_name', 'ward_name', 'assent_name']
    list_filter= ['assent_name', 'phone_number']
    list_per_page= 20
# Register your models here.

class QuestionnaireAdmin (admin.ModelAdmin):
    # list_display = [field.name for field in Questionnaire._meta.get_fields()]
    list_display = ('Qnum', 'Date', 'Date_of_birth', 'Age_year', 'Age_month', 'LGA', 'Ethnicity', 'Religion', 'Duration_years', 'Duration_months',
        'Hospital', 'Family', 'Children', 'Father_education', 'Mother_education', 'Father_occupation',
        'Mother_occupation', 'Father_income', 'Mother_income', 'Total_income_per_month', 'Clinic_visits_per_month',
        'Visits_to_other_centres', 'Percentage_of_income_spent',
        'Aid_from_other_sources', 'How_much', 'Working', 'Care_taker', 'Cost_of_care_taker', 'Extra_time_spent',
        'Stigma', 'Stopped_working', 'Money_foregone', 'Activities_forgone', 'They_are', 'Weight', 'Height', 'BMI', 'Lab_estimation', 'Net_Income',
        )
    list_filter= ['Qnum', 'Stopped_working']
    list_per_page= 20

class TableOfCostAdmin (admin.ModelAdmin):
    list_display = ['Qnum', 'Syringes_Unit_cost','Syringes_Quantity', 'Syringes_Cost_per_month','Needles_Unit_cost',
        'Needles_Quantity', 'Needles_Cost_per_month', 'Glucometer_strips_Unit_cost', 'Glucometer_strips_Quantity',
        'Glucometer_strips_Cost_per_month','Regular_insulin_Unit_cost', 'Regular_insulinQuantity', 'Regular_insulin_Cost_per_month',
        'Basal_insulin_Unit_cost', 'Basal_insulin_Quantity', 'Basal_insulin_Cost_per_month', 'Ice_packs_Unit_cost',
        'Ice_packs_Quantity', 'Ice_packs_Cost_per_month', 'Support_equipment_Unit_cost', 'Support_equipment_Quantity',
        'Support_equipment_Cost_per_month', 'Cost_of_transportation_Unit_cost','Cost_of_transportation_Quantity', 'Cost_of_transportation_Cost_per_month',
        'Item_9', 'Unit_cost_9', 'Quantity_9', 'Cost_per_month_9', 'Item_10', 'Unit_cost_10', 'Quantity_10', 'Cost_per_month_10',
        'Direct_cost', 'Indirect_cost', 'Total_cost', 
        ]  
    list_filter= ['id', 'Qnum', 'Indirect_cost']
    list_per_page= 20
    # list_display = ['id', 'Syringes_Unit_cost','Syringes_Quantity',]

admin.site.register(Media, MediaAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Questionnaire, QuestionnaireAdmin)
admin.site.register(TableOfCost, TableOfCostAdmin)