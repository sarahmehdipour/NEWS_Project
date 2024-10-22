from django.shortcuts import render ,redirect
from .models import News,Category,Tag


def list_news(request):
    news=News.objects.filter(active=True)
    context={'news':news}
    return render(request,'news/listnews.html',context)



# Create your views here.
