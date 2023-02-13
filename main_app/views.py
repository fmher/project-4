from django.shortcuts import render

# Add the following import
from django.http import HttpResponse
from .models import Cars

# Define the home view
def home(request):
    # return HttpResponse('<h1> (╯°□°）╯︵ ┻━┻ </h1>')
    return render(request, 'welcome_page.html')

def cars(request):
    cars = Cars.objects.all()
    # messed up on DB name, so it is carss
    return render(request, 'cars_list.html', {'carss':cars})