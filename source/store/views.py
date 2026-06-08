from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from .forms import ProductSearchForm, ProductForm


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.filter(remainder__gte=1).order_by('category__title','title')
        form = ProductSearchForm(request.GET)
        if form.is_valid():
            search_title = form.cleaned_data.get('search_title')

            if search_title:
                products = products.filter(title__icontains=search_title)
        return render(request, "market/products.html", {'products': products, 'form': form})

def product_view(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'market/product.html', {'product': product})

def product_add_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            return redirect("product", id=product.id)
    else:
        form = ProductForm()
    return render(request, 'market/product_create.html', {'form': form})

def category_add_view(request):
    if request.method == 'GET':
        return render(request, 'market/category_create.html')
    elif request.method == 'POST':
        category = Category.objects.create(
            title=request.POST.get("title"),
            description=request.POST.get("description")
        )
        return redirect("products")
    return None

def product_update_view(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("products")
    else:
        form = ProductForm(instance=product)
    return render(request, 'market/product_update.html', {'product': product, 'form': form})



def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.delete()
        return redirect("products")
    return render(request, "market/product_delete.html", {"product": product})
