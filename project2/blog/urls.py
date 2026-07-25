from django.urls import path
from . import views

urlpatterns = [
    # 1. Change this line so the homepage doesn't call post_details
    path('', views.home, name='home'), 
    
    # 2. Put the post_id variable inside its own dedicated path
    path('post/<int:post_id>/', views.post_details, name='post_details'),
    path('user/<str:username>/', views.user_profile, name='user_profile'),
]
