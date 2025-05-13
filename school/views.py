from django.shortcuts import render,HttpResponse
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request, "home.html")

def contact_us(request):
    return render(request, "contact.html")

def welcome(request):
    return render(request, "welcome.html")
