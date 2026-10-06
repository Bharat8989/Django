from django.urls import path

from . import views


urlpatterns =[
  path('blog/',views.about,name='blog_about'),
  # path('about',view)
]