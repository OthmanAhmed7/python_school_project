from django.shortcuts import render,HttpResponse
from django.http import JsonResponse

from products.models import Products

# Create your views here.
def home(request):
    all_products = Products.objects.all()
    print(all_products)
    context = {}
    context ['products'] = all_products
    return render(request, "products/home.html", context=context)

def contact_us(request):
    return render(request, "products/contact.html")

def welcome(request):
    return render(request, "products/welcome.html")
