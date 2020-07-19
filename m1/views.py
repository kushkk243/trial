from django.shortcuts import render
from django.http.response import HttpResponse


def homeview(request):
    return HttpResponse("Hello World")

# Create your views here.
