from django.urls import path
from . import views

urlpatterns= [
    path('', views.about, name = 'about'),
    path('form/', views.form, name = 'form'),
    path('quest/', views.quest, name = 'quest'),
    path('consentform/', views.consentform, name = 'consentform'),
    path('questionform/', views.questionform, name = 'questionform'),
    path('tocform/', views.tocform, name = 'tocform'),
    path('logoutfunc/', views.logoutfunc, name = 'logoutfunc'),
]