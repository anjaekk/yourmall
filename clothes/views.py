from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def index(request):
    today = datetime.today().date()
    context = {"date":today}
    return render(request, 'clothes/index.html', context=context)

def trend_detail(request, trend):
    context = {"name":trend}
    return render(request, 'clothes/detail.html', context=context)