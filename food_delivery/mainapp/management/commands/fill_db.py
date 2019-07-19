from django.core.management.base import BaseCommand
from mainapp.models import Products, ProductCategory, Restaurant, RestaurantCategory
from django.contrib.auth.models import User
from authapp.models import ShopUser
import json, os

JSON_PATH = 'mainapp/json'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        # категории
        categories = load_from_json('categories')
        ProductCategory.objects.all().delete()
        for category in categories:
            # print(category)
            new_category = ProductCategory(**category)
            new_category.save()

        # рестораны
        restaurants = load_from_json('restaurants')
        Restaurant.objects.all().delete()
        for restaurant in restaurants:
            new_restaurant = Restaurant(**restaurant)
            new_restaurant.save()

        # продукты
        # print(type(load_from_json('products1')))
        products = load_from_json('products')

        Products.objects.all().delete()
        for product in products:
            # print(product)
            restaurant_name = product['restaurant']
            _restaurant = Restaurant.objects.get(name=restaurant_name)
            product['restaurant'] = _restaurant
            category_name = product['category']
            _category = ProductCategory.objects.get(name=category_name)
            product['category'] = _category
            new_product = Products(**product)
            new_product.save()

        # категории ресторанов
        restaurant_category = load_from_json('restauran_category')
        RestaurantCategory.objects.all().delete()
        for RC in restaurant_category:
            restaurant_name = RC['restaurant']
            # print(restaurant_name)
            # print(Restaurant.objects.get(name=restaurant_name))
            _restaurant = Restaurant.objects.get(name=restaurant_name)
            RC['restaurant'] = _restaurant
            category_name = RC['category']
            _category = ProductCategory.objects.get(name=category_name)
            RC['category'] = _category
            new_RC = RestaurantCategory(**RC)
            new_RC.save()

    super_user = ShopUser.objects.create_superuser('user', 'test@test.ru', 'user', age=18)
