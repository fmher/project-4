from django.shortcuts import render

# Add the following import
from django.http import HttpResponse
from .models import Cars

# Define the home view
def home(request):
    # return HttpResponse('<h1> (╯°□°）╯︵ ┻━┻ </h1>')
    cars = Cars.objects.all()
    return render(request, 'welcome_page.html', {'carss':cars})

def cars(request):
    cars = Cars.objects.all()
    # messed up on DB name, so it is carss
    return render(request, 'cars_list.html', {'carss':cars})

def cars_info(request, pk):
    info = Cars.objects.filter(pk = pk)
    # info is only one car and its info
    return render(request, 'car_info.html', {'carss':info})