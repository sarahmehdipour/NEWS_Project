from django.shortcuts import render


def index(request):
    return render(request,'website/news.html')
# Create your views here.
