from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from ordersapp.models import Order
from django.views.generic import DeleteView

class OrderDelete(DeleteView):
    model = Order
    success_url = reverse_lazy('ordersapp:orders_list')
