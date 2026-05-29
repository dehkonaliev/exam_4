from django.shortcuts import render, redirect
from .models import Category, Product
from .forms import NewProductForm
from django.db.models import Q


def home(request):
    if request.method == 'POST':
        search_query = request.POST.get('search', '')
        data = Product.objects.filter(Q(name__icontains=search_query) | Q(desc__icontains=search_query))
        print(data)
    else:
        data = Product.objects.order_by('-created_at')[:10]
    return render(request, 'index.html', {'latest_10':data})

def category(request):
    products = Product.objects.all().order_by('-created_at')[:20]
    categories = Category.objects.all()
    if request.method == "POST" and not request.POST.get('category') == 'all':
        category = request.POST.get('category')
        products = Product.objects.filter(category=category).order_by('-created_at')
        return render(request, 'category.html', {'products':products, 'categories':categories, 'selected_category':category})
    return render(request, 'category.html', {'products':products, 'categories':categories})

def product_detail(request, pk):
    product = Product.objects.filter(pk=pk).first()
    return render(request, 'detail.html', {'product':product})

def product_update(request, pk):
    product = Product.objects.filter(pk=pk).first()
    form = NewProductForm(instance=product)
    if request.method == 'POST':
        form = NewProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('detail', pk=product.pk)
    else:
        form = NewProductForm(instance=product)
    return render(request, 'update.html', {'form':form, 'product':product})

def new_product(request):
    if request.method == 'POST':
        form = NewProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewProductForm()
    return render(request, 'new_product.html', {'form':form})