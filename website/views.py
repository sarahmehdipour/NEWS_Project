from django.shortcuts import render ,redirect
from .forms import ContactForm 
from django.contrib import messages

def index(request):
    return render(request,'website/news.html')


def contact(request):

    if request.method =="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has received successfully")  
            return redirect('/')

    form=ContactForm()

    return render(request,'website/contact.html',{'form':form})


# Create your views here.
