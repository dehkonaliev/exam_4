from django.shortcuts import render, redirect
from .models import Category, Product
from .forms import NewProductForm


def home(request):
    if request.method == 'POST':
        search_query = request.POST.get('search', '')
        data = Product.objects.filter(name__icontains=search_query)
        print(data)
    else:
        data = Product.objects.order_by('-created_at')[:10]
    return render(request, 'index.html', {'latest_10':data})

def category(request):
    products = Product.objects.all()[:20]
    categories = Category.objects.all()
    if request.method == "POST" and not request.POST.get('category') == 'all':
        category = request.POST.get('category')
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products':products, 'categories':categories, 'selected_category':category})
    return render(request, 'category.html', {'products':products, 'categories':categories})

def product_detail(request, pk):
    product = Product.objects.filter(pk=pk).first()
    return render(request, 'detail.html', {'product':product})

def product_update(request):
    return render(request, 'update.html')

def new_product(request):
    if request.method == 'POST':
        form = NewProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewProductForm()
    return render(request, 'new_product.html', {'form':form})