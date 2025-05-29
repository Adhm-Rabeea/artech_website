from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    # return HttpResponse("adhm")
    name = "ARtech adhm rabeea"
    return render(request, "core/index.html",{"name":name})
