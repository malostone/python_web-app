from django.core.management.base import BaseCommand
from mainapp.models import Products, ProductCategory
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
            new_category = ProductCategory(**category)
            new_category.save()


        # продукты
        products = load_from_json('products')
        Products.objects.all().delete()
        for product in products:
            new_product = Products(**product)
            new_product.save()

        super_user = ShopUser.objects.create_superuser('user', 'test@test.ru', 'user', age=18)
