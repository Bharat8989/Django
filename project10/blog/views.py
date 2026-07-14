from django.shortcuts import render

# Create your views here.
def blog(request):
    return render(request,'blog.html')

# def about(request):
#     return render(request,'about.html')




# from django.shortcuts import render

# # Create your views here.
# def home(request):
#     return render(request,'home.html')

# def about(request):
#     return render(request,'about.html')

# from django.shortcuts import render
# from django.http import HttpResponse
# from django.views import View  # <-- Required to make class-based views work

# # Function-Based Views (FBV)
# def home(request):
#     return HttpResponse("Home Page blog")

# def about(request):
#     return HttpResponse("About Page blog")

# def contact(request):
#     return HttpResponse('Contact Page blog')

# # Class-Based View (CBV)
# class Footer(View):
#     def get(self, request):
#         return HttpResponse("Footer Page blog")
