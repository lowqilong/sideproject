from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Sales, Products, Categories

from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.

def single_slug(request, single_slug):
    categories = [c.slug for c in Categories.objects.all()]
    if single_slug in categories:
        matching_products = Products.objects.filter(category__category = single_slug).order_by("published")
    
        return render(request,
                    "main/categories.html",
                    {"products":matching_products})

    products = [p.slug for p in Products.objects.all()]
    if single_slug in products:
        this_product = products.objects.get(slug = single_slug)
        matching_category = Categories.objects.get(category = this_product.category)
        similar_products = Products.objects.filter(category__category = matching_category.category).order_by("published")
            
        return render(request,
                      "main/product.html",
                      {"product": this_product,
                       "similar_products": similar_products})
    
    return redirect("main:homepage")


def homepage(request):
    sales = Sales.objects.all()
    categories = Categories.objects.all()
    products = Products.objects.all()

    return render(request=request,
                  template_name = "main/home.html",
                  context={"sales":sales,
                      "categories":categories,
                      "products":products,
                  })


def signup(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New Account Created: {username}")
            login(request, user)
            messages.info(request, f"You are now logged in as {username}")
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

    form = NewUserForm
    return render(request,
                "main/register.html",
                context={"form":form})



def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("main:homepage")
            else:
                messages.error(request, "Invalid username or password")

        else:
            messages.error(request, "Invalid username or password")

    form = AuthenticationForm()
    return render(request,
                "main/login.html",
                {"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")

