from django.db import models
from django.conf import settings
from mainapp.models import Products, ProductCategory, Restaurant


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    restauran = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)
    price = models.DecimalField(verbose_name='Цена', max_digits=20, decimal_places=2, default=0)

    def get_product_cost(self):
        return self.product.price * self.quantity

    product_cost = property(get_product_cost)

    def get_total_quantity(self):
        items = Basket.objects.filter(user=self.user)
        totalquantity = sum(list(map(lambda x: x.quantity, items)))
        return totalquantity

    total_quantity = property(get_total_quantity)

    def _get_total_cost(self):
        items = Basket.objects.filter(user=self.user)
        totalcost = sum(list(map(lambda x: x.product_cost, items)))
        return totalcost

    total_cost = property(_get_total_cost)

    def get_items(user):
        items = Basket.objects.filter(user=user)
        return items

    items = property(get_items)


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.TextField(verbose_name='Адрес доставки', max_length=300)
    phone = models.PositiveIntegerField(verbose_name='Телефон', default=0)
    is_active = models.BooleanField(verbose_name='активен', default=True)

    def __str__(self):
        return 'Текущий заказ: {}'.format(self.id)

    def get_total_quantity(self):
        items = self.orderitems.select_related()
        return sum(list(map(lambda x: x.quantity, items)))

    def get_product_type_quantity(self):
        items = self.orderitems.select_related()
        return len(items)

    def get_total_cost(self):
        items = self.orderitems.select_related()
        return sum(list(map(lambda x: x.quantity * x.product.price, items)))


class OrderItems(models.Model):
    order = models.ForeignKey(Order, related_name='orderitems', on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)

    def get_product_cost(self):
        return self.product.price * self.quantity

    @staticmethod
    def get_item(self, pk):
        return OrderItem.objects.filter(pk=pk).first()