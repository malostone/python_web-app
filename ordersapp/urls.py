import ordersapp.views as ordersapp
from django.urls import path

app_name="ordersapp"

urlpatterns = [
   path('delete/<int:pk>/', ordersapp.OrderDelete.as_view(), name='order_delete')
]
