from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {});
def about_view(request, *args, **kwargs):
    my_context = {
        "text": "Our Campany is aimed at providing the best services possible",
        "info": "Prices are very decent and made affordable for anyone to purchase our products. Some of which include: ",
        "product_types": ['Perfume: $299.99', 'Balenciaga: $349.99', 'Soft-drinks: $119.99', 'Pasteries: $99.99', 'Chocolates: $499.99']
    }
    return render(request, 'about.html', my_context)
def detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'object': obj
    }
    return render(request, 'product/detail.html' , context)
