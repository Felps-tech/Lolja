from math import ceil
from django.shortcuts import render
from lojinha.models import Product

def index(request):
    products = Product.objects.order_by('product_name')
    context = {'object_list': products}
    return render(request,'index.html', context)

