from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
  return HttpResponse("home page")


def about(request):
  return HttpResponse('hello this is about page')