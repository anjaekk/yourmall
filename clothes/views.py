from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.http import Http404
from clothes.models import Trend
# Create your views here.

def index(request):
    context = dict()
    today = datetime.today().date()
    trends = Trend.objects.all()
    context ["date"] = today
    context["trends"] = trends
    return render(request, 'clothes/index.html', context=context)

def trend_detail(request, pk):
    try:
        context = dict()
        trend = Trend.objects.get(id=pk)
        context["trend"] = trend
    # 404예외처리 
    except Trend.DoesNotExist:
        raise Http404('게시물을 찾을 수 없습니다.')
    
    return render(request, 'clothes/detail.html', context=context)