from django.shortcuts import render

# Add the following import
from django.http import HttpResponse
from .models import Cars

# Define the home view
def home(request):
    # return HttpResponse('<h1> (╯°□°）╯︵ ┻━┻ </h1>')
    cars = Cars.objects.all()
    # named db cars so in django db its carss
    return render(request, 'welcome_page.html', {'carss':cars})

def cars_info(request, pk):
    # find whichevers been clicked 
    info = Cars.objects.filter(pk = pk)
    all_cars = Cars.objects.all()
    # decided to give car its own page, due to possible diff pic size and quality
    # if pk == certain num, gets redirected to specfic page
    if (pk == 1):
        # info refers to specific car
        # all_cars refers to all cars in DB
        # DB is called carss instead of carss due to sql pluralizing automatically
        return render(request, 'model_2.html', {'Cars':info, 'carss':all_cars})
    elif (pk == 2):
        return render(request, 'model_s.html', {'Cars':info, 'carss':all_cars} )
    elif (pk == 4):
        return render(request, 'model_l.html', {'Cars':info, 'carss':all_cars} )
    elif (pk == 5):
        return render(request, 'model_o.html', {'Cars':info, 'carss':all_cars} )


def contact(request):
    cars = Cars.objects.all()
    return render(request, 'contact.html', {'carss':cars})

def legal_terms(request):
    cars = Cars.objects.all()
    return render(request, 'legal_terms.html', {'carss':cars})

# was scrapped
# def overview(request, pk):
#     current_car = Cars.objects.filter(pk = pk)
#     return render(request, 'overview.html', { 'Cars':current_car})