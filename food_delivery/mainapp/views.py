from django.shortcuts import render
from django.views.generic.list import ListView
import random
from .models import Products, ProductCategory, ProductCompany


def get_random_restoran():
    restorans = ProductCompany.objects.all()
    # return restorans[0]
    return random.sample(list(restorans), 1)[0]


def get_hot_products():
    restoran = get_random_restoran()
    products = Products.objects.filter(company__name=restoran.name)
    hot_products = random.sample(list(products), 3)[:2]
    return hot_products


def main(request):
    title = 'Главная'
    hot_products = get_hot_products()
    categories = ProductCategory.objects.all()
    content = {'title': title,
               'products': hot_products,
               'categories': categories,
               }
    return render(request, 'mainapp/index.html', content)


class CompanyCatalogView(ListView):
    model = ProductCompany
    template_name = 'mainapp/catalog.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        return context
