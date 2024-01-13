# Create your views here.
from django.shortcuts import render

from apiculture_app.models import Beeyard

def welcome_with_template(request):
    return render(request, 'welcome.html',)

def hive_list(request):
    beeyards = Beeyard.objects.all().prefetch_related("hives")
    return render(request, 'show_beeyard.html', {'beeyards': beeyards},)

