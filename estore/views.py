# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import redirect, render
from .models import Product
from .forms import ProductForm

# Create your views here.
def product_index(request):
    products = Product.objects.all()
    return render(request, 'estore/product_index.html', {'products': products})

def product_new(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            return redirect('product_index')
    else:
        form = ProductForm()
    return render(request, 'estore/product_new.html', {'form': form})
