from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def helo(request):
    return HttpResponse("<h1>category is working</h1>")
