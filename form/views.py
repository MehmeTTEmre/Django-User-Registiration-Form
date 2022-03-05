from django.shortcuts import render, redirect
from .forms import RecipeForm


# Create your views here.

def form(request):
    return render(request, "form.html")

def form_details(request):
    return render(request, "form-details.html")

def create_recipe(request):
    if request.method == "GET":
        form = RecipeForm()
        return render(request, 'form-details.html', {"form":form})
