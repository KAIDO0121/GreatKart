from django.shortcuts import render, get_object_or_404
from store.models import Product
from category.models import Category

def store(request, category_slug = None):
    products = Product.objects.all().filter(is_available= True)
 
    if category_slug != None:
        category_name = get_object_or_404(Category, slug= category_slug)
        products = Product.objects.all().filter(is_available= True, category= category_name)   
    products_count = products.count()
    context = {
        "products": products,
        "products_count": products_count
    }
    return render(request, 'store.html', context)
def product_detail(request, category_slug, product_slug) :
    try:
        product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e

    context = {
        'product': product
    }

    return render(request, 'product-detail.html', context)

# Create your views here.
