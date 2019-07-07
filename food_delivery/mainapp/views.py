from django.shortcuts import render
from django.views.generic.list import ListView
import random
from .models import Products, ProductCategory
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpRequest


def main(request):
    title = 'Главная'
    categories = ProductCategory.objects.all()
    content = {'title': title,
               'categories': categories,
               }
    return render(request, 'mainapp/index.html', content)


# class CompanyCatalogView(ListView):
#     model = ProductCompany
#     template_name = 'mainapp/catalog.html'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['categories'] = ProductCategory.objects.all()
#         return context


# def restoran_of_category(request, pk=None):
#     # links_menu = ProductCategory.objects.filter(is_active=True)
#
#     # basket = get_basket(request.user)
#
#     if pk != None:
#         if pk == 0:
#             restorans = ProductCompany.objects.all()
#             category = {'name': 'все', 'pk': 0}
#         else:
#             category = get_object_or_404(ProductCategory, pk=int(pk))
#             products = Products.objects.filter(category__pk=int(pk))
#             restorans = []
#             for product in products:
#                 if ProductCompany.objects.get(name=product.company) in restorans:
#                     continue
#                 else:
#                     restorans.append(ProductCompany.objects.get(name=product.company))
#     title = 'Рестораны с категорией {}'.format(category.name)
#
#     content = {
#         'title': title,
#         'category': category,
#         'restorans': restorans,
#
#     }
#
#     return render(request, 'mainapp/restorans_list.html', content)


def products(request, pk=None):
    links_menu = ProductCategory.objects.all()

    if pk == 0:
        category = {'name': 'все', 'pk': 0}
        products = Products.objects.all()
        title = "Все продукты"
    else:
        category = get_object_or_404(ProductCategory, pk=pk)
        products = Products.objects.filter(category__pk=pk)

        title = 'Продукты категории: {}'.format(category.name)

    content = {
        'title': title,
        'links_menu': links_menu,
        'category': category,
        'products': products,
        # 'basket': basket,
    }

    return render(request, 'mainapp/products.html', content)
