from django.shortcuts import render
from django.http import HttpResponse
from django.views import View  # <-- Required to make class-based views work

# Function-Based Views (FBV)
def home(request):
    return HttpResponse("Home Page shop")

def about(request):
    return HttpResponse("About Page shop")

def contact(request):
    return HttpResponse('Contact Page shop')

# Class-Based View (CBV)
class Footer(View):
    def get(self, request):
        return HttpResponse("Footer Page shop")
