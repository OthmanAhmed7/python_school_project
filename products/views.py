from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse

from products.models import Products

# Create your views here.
def home(request):
    all_products = Products.objects.all()
    context = {}
    context ['products'] = all_products
    return render(request, "products/home.html", context=context)

def contact_us(request):
    return render(request, "products/contact.html")

def welcome(request):
    return render(request, "products/welcome.html")

def upload_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_product')
    else:
        form = ProductForm()
    return render(request, 'products/upload.html', {'form': form})