from django.shortcuts import render
import random


def get_random_restoran():
    restorans = Restorans.objects.all()

    return random.sample(list(restorans), 1)[0]


def get_hot_products():
    restoran = get_random_restoran()
    products = Products.object.filter(restoran=restoran, is_active=True)
    hot_products = random.sample(list(products), 3)
    return hot_products


def main(request):
    title = 'Главная'
    hot_products = get_hot_products()

    content = {'title': title,
               'products': products,
               }
    return render(request, 'mainapp/index.html', content)
