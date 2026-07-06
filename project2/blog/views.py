from django.shortcuts import render
from django.http import HttpResponse

# You are missing this exact function!
def home(request):
    return HttpResponse("<h1>Welcome to the Blog Homepage!</h1>")

def post_details(request, post_id):
    return HttpResponse(f'<h1>show blog post {post_id}</h1>')

def user_profile(request, username):
    return HttpResponse(f'<h1>profile of user: {username}</h1>')
