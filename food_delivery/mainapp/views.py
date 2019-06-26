from django.shortcuts import render
import random
from .models import Product, ProductCategory, ProductCompany


def get_random_restoran():
    restorans = ProductCompany.objects.all()
    # return restorans[0]
    return random.sample(list(restorans), 1)[0]


def get_hot_products():
    restoran = get_random_restoran()
    products = Product.objects.filter(company__name=restoran.name)
    hot_products = random.sample(list(products), 3)[:2]
    return hot_products


def main(request):
    title = 'Главная'
    hot_products = get_hot_products()

    content = {'title': title,
               'products': hot_products,
               }
    return render(request, 'mainapp/index.html', content)
