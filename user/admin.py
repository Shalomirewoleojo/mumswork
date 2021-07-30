from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea
# Register your models here.

class UserAdminConfig(UserAdmin):
    search_fields= ('assent_name', 'ward_name', 'last_name')
    list_filter= ('ward_name', 'last_name', 'first_name')
    ordering = ('-start_date',)
    list_display = ('username', 'ward_name', 'assent_name', 'last_name', 'is_active', 'is_staff')
    list_per_page= 5
    fieldsets = (
        (None, {'fields': ('username', 'password', 'first_name')}),
        ('Personal info', {'fields': ('last_name', 'ward_name', 'phone_number', 'assent_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('start_date',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'phone_number', 'ward_name', 'assent_name', 'password1', 'password2', 'is_active', 'is_staff'),
        }),
    )

admin.site.register(CustomUser, UserAdminConfig)