from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
# functions based view 
#FBV
def home(request):
    return HttpResponse("home")


# Class based view (CBV)

class About(View):
    def get(self,request):
        return HttpResponse('hello about page ')