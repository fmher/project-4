from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cars/', views.cars, name='cars'),
    path('cars/<int:pk>/info', views.cars_info, name='cars_info')
]