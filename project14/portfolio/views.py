from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import StudentPortfolio
def student_list(request):
    student_list=StudentPortfolio.objects.all()
    return render(request,'portfolio/student_list.html',{'student_list':student_list})