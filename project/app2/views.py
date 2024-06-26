from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home2(request):
    return HttpResponse("<h1>welcome to app 2 home page...</h1>")