import ordersapp.views as ordersapp
from django.urls import path

app_name="ordersapp"

urlpatterns = [
	path('create/', ordersapp.OrderList.as_view(), name='order_create')
	# path('delete/<int:pk>/', ordersapp.OrderDelete, name='order_delete')
]
