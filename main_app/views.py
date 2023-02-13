from django.shortcuts import render

# Add the following import
from django.http import HttpResponse
from .models import Cars

# Define the home view
def home(request):
    # return HttpResponse('<h1> (╯°□°）╯︵ ┻━┻ </h1>')
    cars = Cars.objects.all()
    return render(request, 'welcome_page.html', {'carss':cars})

def cars_info(request, pk):
    info = Cars.objects.filter(pk = pk)
    all_cars = Cars.objects.all()
    # info is only one car and its info
    return render(request, 'car_info.html', {'Cars':info, 'carss':all_cars})