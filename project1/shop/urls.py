from django.urls import path
from . import views

urlpatterns = [
    # Calling Function-Based Views
    path('', views.home, name='home'),
    path('about/', views.about),
    path('contact/', views.contact, name='contact'),
    
    # Calling Class-Based View
    path('footer/', views.Footer.as_view(), name='footer'),
]
