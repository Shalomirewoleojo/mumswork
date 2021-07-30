from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate, login, logout

from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import get_user_model 

# Create your views here.

def about (request):
    med = Media.objects.get(pk=1)

    context = {
        'med': med,
    }

    return render(request, 'about.html', context)
    # return HttpResponse('Lets get started')


def form (request):
    med = Media.objects.get(pk=1)

    context = {
        'med': med,
    }

    return render(request, 'form.html', context)

def consentform(request):
    form = ConsentForm()
    if request.method == 'POST':
        form = ConsentForm(request.POST)
        if form.is_valid():
            myconsent = form.save()
            p = UserProfile(user1=myconsent)
            # p.user = myconsent.username
            p.first_name = myconsent.first_name
            p.last_name = myconsent.last_name
            p.ward_name = myconsent.ward_name
            p.assent_name = myconsent.assent_name
            p.phone_number = myconsent.phone_number
            p.save()
            login(request, myconsent)
            return redirect ('quest')
        else:
            messages.warning(request, form.errors)
            return redirect ('form')


    if request.method == 'POST':
        form = ConsentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('quest')
        else:
            messages.warning (request, form.errors)
            return redirect ('form')

    med = Media.objects.get(pk=1)

    context = {
        'med': med,
    }

    return render(request, 'form.html', context)



@login_required(login_url='/form')
def quest (request):
    med = Media.objects.get(pk=1)
    # question = Questionnaire.objects.filter(pk=id)
    # toc = TableOfCost.objects.filter(pk=id)

    context = {
        'med': med,
        # 'question': question,
        # 'toc': toc,
    }

    return render(request, 'questionnaire.html', context)


@login_required(login_url='/form')
def questionform (request):
    form = QuestionnaireForm()
    if request.method == 'POST':
        form = QuestionnaireForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('tocform')
        else:
            messages.warning (request, form.errors)
            return redirect ('questionform')

    med = Media.objects.get(pk=1)
    user_no = get_user_model()
    # num = user_no.objects.filter(is_superuser=False)

    context = {
        'med': med,
        'form': form,
        # 'num': num,
    }

    return render(request, 'questionnaire.html', context)


@login_required(login_url='/form')
def tocform (request):
    form = TableOfCostForm()
    if request.method == 'POST':
        form = TableOfCostForm(request.POST)
        if form.is_valid():
            # q= TableOfCost()
            # self= UserProfile()
            # q.question= self.user1.username
            # q.save()
            form.save()
            return redirect ('logoutfunc')
        else:
            messages.warning (request, form.errors)
            return redirect('tocform')

    med = Media.objects.get(pk=1)

    context = {
        'med': med,
        'form': form,
    }

    return render(request, 'toc.html', context)


def logoutfunc (request):
    logout(request)
    return redirect('about')