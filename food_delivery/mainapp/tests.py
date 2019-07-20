from django.test import TestCase
from django.test.client import Client
from mainapp.models import Product, ProductCategory, Restaurant, RestaurantCategory
from django.core.management import call_command


class TestMainappSmoke(TestCase):
    def setUp(self):
        call_command('flush', '--noinput')
        call_command('loaddata', 'test_db.json')
        self.client = Client()

    def test_mainapp_urls(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        for restaurant in Restaurant:
            categories = RestaurantCategory.objects.filter(restaurant=restaurant)
            for category in categories:

                response = self.client.get(f'/products_list/{restaurant.pk}/{category.category.pk}')
                self.assertEqual(response.status_code, 200)

    def tearDown(self):
        call_command('sqlsequencereset', 'mainapp', 'authapp', \
                     'basketapp')
