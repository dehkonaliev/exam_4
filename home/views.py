from django.shortcuts import render


def home(request):
    return render(request, 'index.html')

def category(request):
    return render(request, 'category.html')

def product_detail(request):
    return render(request, 'detail.html')

def product_update(request):
    return render(request, 'update.html')