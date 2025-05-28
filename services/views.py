from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def our_services(request):
  return HttpResponse("Our Services")
