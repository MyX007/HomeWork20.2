import json

from main.models import Category, Product
from django.core.management import BaseCommand


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('main_data.json', "r", encoding="UTF-8") as file:
            json_categories = json.load(file)
            categories = []
            for category in json_categories:
                if category['model'] == 'main.category':
                    categories.append(category)
            return categories

    @staticmethod
    def json_read_products():
        with open('main_data.json', "r", encoding="UTF-8") as file:
            json_products = json.load(file)
            products = []
            for product in json_products:
                if product['model'] == 'main.product':
                    products.append(product)
            return products

    def handle(self, *args, **options):

        product_for_create = []
        category_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(
                Category(name=category['fields']['name'], description=category['fields']['description'])
            )

        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product_for_create.append(
                Product(name=product['fields']['name'],
                        description=product['fields']['description'],
                        category=Category.objects.get(pk=product['fields']['category']),
                        img=product['fields']['img'],
                        price=product['fields']['price'], created_at=product['fields']['created_at'],
                        updated_at=product['fields']['updated_at'])
            )

        Product.objects.bulk_create(product_for_create)
