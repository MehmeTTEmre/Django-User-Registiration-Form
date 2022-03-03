from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request, "home.html", {})

def register(request):
    return render(request, "home.html", {"link": "http://127.0.0.1:8000/register/"})

def login(request):
    return render(request, "home.html", {"link2": "http://127.0.0.1:8000/login/"})