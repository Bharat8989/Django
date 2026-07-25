from django.urls import path
from . import views

urlpatterns = [
    # Calling Function-Based Views
    path('', views.blog, name='blog'),
    # path('about/', views.about, name='about'),
   
]
