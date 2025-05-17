from django.shortcuts import render,HttpResponse
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request, "school/home.html")

def contact_us(request):
    return render(request, "school/contact.html")

def welcome(request):
    return render(request, "school/welcome.html")
