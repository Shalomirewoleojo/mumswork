from django.db import models
from django.conf import settings
from datetime import date
import datetime
# from django.dispatch import receiver
# from django.db.models.signals import post_save
from django.conf import settings
from django.contrib.auth import get_user_model


from user.models import CustomUser
# Create your models here.


class Media (models.Model):
    title = models.CharField(max_length=20)
    img = models.ImageField(null=True, blank=True, upload_to= 'images/')
    logo = models.ImageField(null=True, blank=True, upload_to= 'images/')
    favicon = models.ImageField(null=True, blank=True, upload_to= 'images/')

    def __str__(self):
        return self.title

class UserProfile (models.Model):
    user1 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, default='Mojibola')
    last_name = models.CharField(max_length=50, default='Ernest')
    phone_number = models.DecimalField(blank=True, null=True, max_digits=11, decimal_places=0)
    ward_name = models.CharField(max_length=50) 
    assent_name = models.CharField(null=True, blank=True, max_length=50)

    def __str__(self):
        return self.user1.username

    # instance.userprofile.save()

    @property
    def username(self):
        if self.user_id is not None: 
            return self.user.first_name + ' ' + self.user.last_name + '[' + self.user.username + ']'

    class Meta:
        db_table = 'userprofile'
        managed = True
        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfiles'


class Questionnaire (models.Model):
    # user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    # user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True) 

    Qnum = models.PositiveSmallIntegerField(default=1, unique=True)
    Date = models.DateField(default=datetime.date(2021, 3, 23))
    Date_of_birth = models.DateField(default=datetime.date(2021, 3, 23))
    Age_year= models.PositiveSmallIntegerField(default=0)
    Age_month= models.PositiveSmallIntegerField(default=5)
    LGA= models.CharField(max_length=20)
    Ethnicity= models.CharField(max_length=10)
    Religion = models.CharField(max_length=15)
    Duration_years = models.PositiveSmallIntegerField()
    Duration_months = models.PositiveSmallIntegerField()
    Hospital = models.CharField(max_length=200)
    Family = models.CharField(max_length=50)
    Children = models.PositiveSmallIntegerField()
    Father_education = models.CharField(max_length=50)
    Mother_education = models.CharField(max_length=50)
    Father_occupation = models.CharField(max_length=50)
    Mother_occupation = models.CharField(max_length=50)
    Father_income = models.CharField(max_length=200)
    Mother_income = models.CharField(max_length=200)
    Total_income_per_month = models.PositiveIntegerField()
    Clinic_visits_per_month = models.PositiveIntegerField()
    Visits_to_other_centres = models.PositiveSmallIntegerField(blank=True, null=True)

    
    
    Percentage_of_income_spent = models.PositiveSmallIntegerField()
    Aid_from_other_sources= models.CharField(max_length=3)
    How_much = models.PositiveIntegerField( blank=True, null=True, default=0)
    Working= models.CharField(max_length=3)
    Care_taker = models.CharField(max_length=200, blank=True, null=True)
    Cost_of_care_taker = models.PositiveIntegerField(blank=True, null=True, default=0)
    Extra_time_spent = models.PositiveSmallIntegerField()
    Stigma = models.CharField(max_length=200, blank=True, null=True)
    Stopped_working= models.CharField(max_length=3)
    Money_foregone = models.PositiveSmallIntegerField(blank=True, null=True)
    Activities_forgone= models.CharField(max_length=3)
    They_are = models.CharField(max_length=200, blank=True, null=True)
    Weight = models.PositiveSmallIntegerField()
    Height = models.PositiveSmallIntegerField()
    BMI = models.PositiveSmallIntegerField()
    Lab_estimation= models.PositiveSmallIntegerField()

    def __str__(self):
        return  str(self.Qnum)

    @property
    def BMI (self):
        return(self.Weight/self.Height**2)

    @property
    def How_much1 (self):
        if self.How_much is not None:
            return (self.How_much)
        else:
            return (0)
    @property
    def Cost_of_care_taker1 (self):
        if self.Cost_of_care_taker is not None:
            return (self.Cost_of_care_taker)          
        else:
            return (0)

    @property
    def Net_Income(self):
        return(
            self.Total_income_per_month + self.How_much1 - self.Cost_of_care_taker1
        )
    


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def update_questionnaire_signal(sender, instance, created, **kwargs):
#     if created:
#         Questionnaire.objects.create(user=instance)
    # instance.questionnaire.save()




class TableOfCost(models.Model):
    # question = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, default='0')
    # user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)

    Qnum = models.PositiveSmallIntegerField(default=1, unique=True)
    Syringes_Unit_cost = models.IntegerField()
    Syringes_Quantity = models.IntegerField()
    Syringes_Cost_per_month = models.IntegerField()

    Needles_Unit_cost = models.IntegerField()
    Needles_Quantity = models.IntegerField()
    Needles_Cost_per_month = models.IntegerField()

    Glucometer_strips_Unit_cost = models.IntegerField()
    Glucometer_strips_Quantity = models.IntegerField()
    Glucometer_strips_Cost_per_month = models.IntegerField()

    Regular_insulin_Unit_cost = models.IntegerField()
    Regular_insulinQuantity = models.IntegerField()
    Regular_insulin_Cost_per_month = models.IntegerField()

    Basal_insulin_Unit_cost = models.IntegerField()
    Basal_insulin_Quantity = models.IntegerField()
    Basal_insulin_Cost_per_month = models.IntegerField()

    Ice_packs_Unit_cost = models.IntegerField()
    Ice_packs_Quantity = models.IntegerField()
    Ice_packs_Cost_per_month = models.IntegerField()

    Support_equipment_Unit_cost = models.IntegerField()
    Support_equipment_Quantity = models.IntegerField()
    Support_equipment_Cost_per_month = models.IntegerField()

    Cost_of_transportation_Unit_cost = models.IntegerField()
    Cost_of_transportation_Quantity = models.IntegerField()
    Cost_of_transportation_Cost_per_month = models.IntegerField()

    Item_9 = models.CharField(max_length=15, blank=True, null=True)
    Unit_cost_9 = models.IntegerField(default=0, blank=True, null=True)
    Quantity_9 = models.IntegerField(default=0, blank=True, null=True)
    Cost_per_month_9 = models.IntegerField(default=0, blank=True, null=True)

    Item_10 = models.CharField(max_length=15, blank=True, null=True)
    Unit_cost_10 = models.IntegerField(default=0, blank=True, null=True)
    Quantity_10 = models.IntegerField(default=0, blank=True, null=True)
    Cost_per_month_10 = models.IntegerField(default=0, blank=True, null=True)

    Direct_cost = models.PositiveIntegerField()
    Indirect_cost = models.PositiveIntegerField( blank=True, null=True)
    Total_cost = models.PositiveIntegerField()

    # def __str__(self):
    #     return self.id

    @property
    def Syringes_Cost_per_month (self):
        if self.Syringes_Quantity is not None:
            return (self.Syringes_Unit_cost * self.Syringes_Quantity)
    @property
    def Needles_Cost_per_month (self):
        if self.Needles_Quantity is not None:
            return (self.Needles_Unit_cost * self.Needles_Quantity)
    @property
    def Glucometer_strips_Cost_per_month (self):
        if self.Glucometer_strips_Quantity is not None:
            return (self.Glucometer_strips_Unit_cost * self.Glucometer_strips_Quantity)
    @property
    def Regular_insulin_Cost_per_month (self):
        if self.Regular_insulinQuantity is not None:
            return (self.Regular_insulin_Unit_cost * self.Regular_insulinQuantity)
    @property
    def Basal_insulin_Cost_per_month (self):
        if self.Basal_insulin_Quantity is not None:
            return (self.Basal_insulin_Unit_cost * self.Basal_insulin_Quantity)
    @property
    def Ice_packs_Cost_per_month (self):
        if self.Ice_packs_Quantity is not None:
            return (self.Ice_packs_Unit_cost * self.Ice_packs_Quantity)
    @property
    def Support_equipment_Cost_per_month (self):
        if self.Support_equipment_Quantity is not None:
            return (self.Support_equipment_Unit_cost * self.Support_equipment_Quantity)
    @property
    def Cost_of_transportation_Cost_per_month (self):
        if self.Cost_of_transportation_Quantity is not None:
            return (self.Cost_of_transportation_Unit_cost * self.Cost_of_transportation_Quantity)
    @property
    def Cost_per_month_9 (self):
        if self.Quantity_9 is not None:
            return (self.Unit_cost_9 * self.Quantity_9)
        else:
            return (0)
    @property
    def Cost_per_month_10 (self):
        if self.Quantity_10 is not None:
            return (self.Unit_cost_10 * self.Quantity_10)          
        else:
            return (0)


    @property
    def Direct_cost(self):
        return(self.Syringes_Cost_per_month + self.Needles_Cost_per_month + self.Glucometer_strips_Cost_per_month
    + self.Regular_insulin_Cost_per_month  + self.Basal_insulin_Cost_per_month + self.Ice_packs_Cost_per_month
    + self.Support_equipment_Cost_per_month + self.Cost_of_transportation_Cost_per_month + self.Cost_per_month_9 + self.Cost_per_month_10)

    @property
    def Total_cost(self):
        if self.Indirect_cost is not None:
            return (self.Direct_cost + self.Indirect_cost)
        else:
            return(self.Direct_cost)
