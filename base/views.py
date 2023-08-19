from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render

from .models import *
from .forms import *


def home_page(request):
    products = Product.objects.filter(sold=False)
    context = {'products': products}
    return render(request, 'base/home.html', context)


def add_product(request: HttpRequest):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            return redirect('admin_page')
    else:
        form = ProductForm()
    context = {'form': form, 'title': 'Add Product',
               'submit': 'add', 'admin': True}
    return render(request, 'base/form.html', context)


def edit_product(request: HttpRequest, pk: int):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save()
            return redirect('admin_page')
    else:
        form = ProductForm(instance=product)
    context = {'form': form, 'title': 'Edit Product',
               'submit': 'Edit', 'admin': True}
    return render(request, 'base/form.html', context)


def delete_product(request: HttpRequest, pk: int):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect("admin_page")


def check_product(request: HttpRequest, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'base/product.html', context)


def buy_product(request: HttpRequest, pk):
    product = get_object_or_404(Product, pk=pk)
    product.sold = True
    product.save()
    return redirect('home')


def admin_page(request):
    products = Product.objects.filter(sold=False)
    context = {'products': products, 'admin': True}
    return render(request, 'base/home.html', context)
