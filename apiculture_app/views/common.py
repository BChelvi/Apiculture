# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from apiculture_app.models import Hive

def welcome_with_template(request):
    return render(request, 'welcome.html',)


def hive_list(request):
    hives = Hive.objects.all()
    return render(request, 'show_beeyard.html', {'hives': hives})