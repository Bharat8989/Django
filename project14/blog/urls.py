from django.urls import path
from . import views

urlpatterns = [
    # functional based view
    path('',views.home, name='home'),
    # class based views (cbv)
    path('about/', views.About.as_view() , name='about'),
]
