from django.urls import path
from . import views

urlpatterns = [
    # functional based view
    path('',views.student_list, name='student_list'),
    # class based views (cbv)
    # path('about/', views.About.as_view() , name='about'),
    
]
    