from django.shortcuts import render ,redirect
from .models import News,Category,Tag


def list_news(request ,**kwargs):
    news=News.objects.filter(active=True)

    if kwargs.get('category'):
        news=news.filter(category__title=kwargs['category'])

    
    if kwargs.get('tag'):
         news=news.filter(Tag__title=kwargs['tag'])
        


    context={'news':news}
    return render(request,'news/listnews.html',context)



def detail_news(request,num):
    new=News.objects.get(id=num)
    context={'new':new}
    return render(request,'news/detailnews.html',context)



# Create your views here.
