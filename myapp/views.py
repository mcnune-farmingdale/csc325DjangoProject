from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse("<h1>Hello, World! Welcome to my Django application!</h1>")

def about(request):
    return HttpResponse("<h1>About Page</h1><p>This is the about page of my Django application.</p>")

def contact(request):
    return HttpResponse("<h1>Contact Page</h1><p>Please fill out the form below and we will get back to you as soon as possible.</p>")