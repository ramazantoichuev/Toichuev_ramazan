from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category



def products_view(request):
    products = Product.objects.all()
    return render(request, "market/products.html", {'products':products})


def product_view(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'market/product.html', {'product': product})

def product_add_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        return render(request,'market/product_create.html',{'categories': categories}
        )
    elif request.method == 'POST':
        product = Product.objects.create(
            title=request.POST.get("title"),
            description=request.POST.get("description"),
            category_id=request.POST.get("category"),
            price=request.POST.get("price"),
            image=request.POST.get("image"),
        )
        return redirect("product", id = product.id)
    return None

def category_add_view(request):
    if request.method == 'GET':
        return render(request, 'market/category_create.html')
    elif request.method == 'POST':
        product = Category.objects.create(
            title=request.POST.get("title"),
            description=request.POST.get("description")
        )
        return redirect("products")
    return None