from django.core.management.base import BaseCommand
from api.models import Book

import csv

class Command(BaseCommand):

    def handle(self, *args, **options):
        keys = ['name', 'pages']
        books = Book.objects.values(*keys)
        with open('books.csv', 'w') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            page = 1
            size = 2000
            while paginated := books[(page-1)*size:page*size]:
                writer.writerows(paginated)
                page += 1
