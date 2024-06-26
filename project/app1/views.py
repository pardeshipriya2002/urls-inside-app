from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def home1(request):
    return HttpResponse("<h1>Welcome to app 1 page....!!</h1>")