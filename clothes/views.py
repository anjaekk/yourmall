from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.http import Http404

# Create your views here.

def index(request):
    today = datetime.today().date()
    context = {"date":today}
    return render(request, 'clothes/index.html', context=context)

def trend_detail(request, trend):
    context = dict()
    if trend == "2021ss" :
        context["name"] = "S/S 2021"
        context["description"] = "2021년 Spring/Summer 트렌드"
        context["img_path"] = "clothes/images/2021ss.jpg"
    else:
        raise Http404()
    return render(request, 'clothes/detail.html', context=context)