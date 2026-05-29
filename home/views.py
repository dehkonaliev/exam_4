from django.shortcuts import render
from .models import Category, Product


def home(request):
    latest_10 = Product.objects.order_by('-created_at')[:10]
    
    return render(request, 'index.html', {'latest_10':latest_10})

def category(request):
    return render(request, 'category.html')

def product_detail(request):
    return render(request, 'detail.html')

def product_update(request):
    return render(request, 'update.html')

def new_product(request):
    return render(request, 'new_product.html')