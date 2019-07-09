from django.shortcuts import render
from django.views.generic.list import ListView
import random
from .models import Products, ProductCategory, Restaurant
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpRequest


def main(request):
    title = 'Главная'
    categories = ProductCategory.objects.all()
    content = {'title': title,
               'categories': categories,
               }
    return render(request, 'mainapp/index.html', content)


def restaurants(request, pk=None):
    if pk == 0:
        restaurant_list = Restaurant.objects.all()
        title = "Все рестораны"
    else:
        category = get_object_or_404(ProductCategory, pk=pk)
        restaurant_list = Restaurant.objects.filter(category__pk=pk)
        title = f'Рестораны, доставляющие {category.name}'

    content = {
        'title': title,
        'restaurant_list': restaurant_list,
    }
    return render(request, 'mainapp/catalog.html', content)


def products(request, pk=None):
    links_menu = ProductCategory.objects.all()

    if pk == 0:
        category = {'name': 'все', 'pk': 0}
        products = Products.objects.all()
        title = "Все продукты"
    else:
        category = get_object_or_404(ProductCategory, pk=pk)
        products = Products.objects.filter(restaurant__pk=pk)

        title = f'Продукты ресторана: {category.name}'

    content = {
        'title': title,
        'links_menu': links_menu,
        'category': category,
        'products': products,
        # 'basket': basket,
    }

    return render(request, 'mainapp/products.html', content)
