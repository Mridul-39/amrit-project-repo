from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def contact(request):
    return render(request, 'contactus.html')

def getstarted(request):
    return render(request, 'getstarted.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def services(request):
    return render(request, 'services.html')