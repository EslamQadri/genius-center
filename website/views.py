from django.shortcuts import render
from website.models import Train, Coures


# Create your views here.
def home(request):
    return render(request, "index.html")


def couress(request):
    
    
    

    return render(request, "couress.html", {"Coures": Coures.objects.all()})


def training(request):
    return render(request, "training.html", {"Train": Train.objects.all()})
