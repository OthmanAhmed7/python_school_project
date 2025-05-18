from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Products

def home(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.error(request, "You must be logged in to create a product.")
            return redirect('login')

        try:
            name = request.POST.get('name')
            category = request.POST.get('category')
            ex_date = request.POST.get('ex_date')
            description = request.POST.get('description')
            price = request.POST.get('price')
            country = request.POST.get('country')
            image = request.FILES.get('image')

            if not all([name, category, ex_date, description, price, country, image]):
                all_products = Products.objects.all()
                context = {
                    'products': all_products,
                    'error': 'All fields are required. Please fill out the form completely.'
                }
                return render(request, "products/home.html", context)

            Products.objects.create(
                name=name,
                category=category,
                ex_date=ex_date,
                description=description,
                price=price,
                country=country,
                image=image,
                user=request.user
            )
            messages.success(request, "Product created successfully.")
            return redirect('home')

        except Exception as e:
            all_products = Products.objects.all()
            context = {
                'products': all_products,
                'error': f'Error creating product: {str(e)}'
            }
            return render(request, "products/home.html", context)

    else:
        all_products = Products.objects.all()
        context = {'products': all_products}
        return render(request, "products/home.html", context)

def contact_us(request):
    return render(request, "products/contact.html")

def welcome(request):
    return render(request, "products/welcome.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully.")
            return redirect('home')
        else:
            return render(request, "registration/login.html", {'error': 'Invalid username or password.'})
    return render(request, "registration/login.html")

def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return render(request, "registration/register.html", {'error': 'Passwords do not match.'})

        if User.objects.filter(username=username).exists():
            return render(request, "registration/register.html", {'error': 'Username already taken.'})

        try:
            user = User.objects.create_user(username=username, password=password1)
            login(request, user)
            messages.success(request, "Registered and logged in successfully.")
            return redirect('home')
        except Exception as e:
            return render(request, "registration/register.html", {'error': f'Error registering: {str(e)}'})

    return render(request, "registration/register.html")

def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('welcome')

@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    if product.user != request.user and product.user is not None:
        messages.error(request, "You can only edit your own products.")
        return redirect('home')

    if request.method == "POST":
        try:
            name = request.POST.get('name')
            category = request.POST.get('category')
            ex_date = request.POST.get('ex_date')
            description = request.POST.get('description')
            price = request.POST.get('price')
            country = request.POST.get('country')
            image = request.FILES.get('image')

            if not all([name, category, ex_date, description, price, country]):
                context = {'product': product, 'error': 'All fields (except image) are required.'}
                return render(request, "products/edit_product.html", context)

            product.name = name
            product.category = category
            product.ex_date = ex_date
            product.description = description
            product.price = price
            product.country = country
            if image:
                product.image = image
            product.save()

            messages.success(request, "Product updated successfully.")
            return redirect('home')

        except Exception as e:
            context = {'product': product, 'error': f'Error updating product: {str(e)}'}
            return render(request, "products/edit_product.html", context)

    return render(request, "products/edit_product.html", {'product': product})

@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    if product.user != request.user and product.user is not None:
        messages.error(request, "You can only delete your own products.")
        return redirect('home')

    if request.method == "POST":
        product.delete()
        messages.success(request, "Product deleted successfully.")
        return redirect('home')
    return redirect('home')