from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome_with_html(request):
    return render(request, 'welcome.html')

def show_beeyard_with_html(request):
    return render(request, 'show_beeyard.html')
