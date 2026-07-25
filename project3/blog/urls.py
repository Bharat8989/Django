from django.urls import path
from . import views

urlpatterns = [
    # 1. Change this line so the homepage doesn't call post_details
    # path('', views.home, name='home'), 
     path('post_list/', views.post_list, name='post_list'),
    # 2. Put the post_id variable inside its own dedicated path
   
]
