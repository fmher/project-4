from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pk>', views.cars_info, name='cars_info'),
    path('contact', views.contact, name='contact'),
    path('legalterms', views.legal_terms, name='legal_terms'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)