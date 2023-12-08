from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        payments_list = [
            {'name': 'apple', 'price': 130, 'category_id': 6},
            {'name': 'cucumber', 'price': 120, 'category_id': 5},
            {'name': 'chicken', 'price': 100, 'category_id': 7},
            {'name': 'mussels', 'price': 700, 'category_id': 8},
        ]