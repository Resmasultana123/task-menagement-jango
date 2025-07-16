from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1 style='color: blue'> welcome sir </h2>")
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Tasks app home page!")
