from django.shortcuts import render
from .models import Product
# Create your views here.


def product(request):
    product = Product.objects.all()

    return render(request, "products/product.html",{'products':product})


def products(request):
    return render(request, "products/products.html")
