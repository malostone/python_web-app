from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns =[
    path('restaurants/<int:pk>/', mainapp.restaurants, name='restaurants'),
    path('products/<int:pk>/', mainapp.products, name='products'),
]