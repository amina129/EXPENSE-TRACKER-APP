from datetime import datetime
from decimal import Decimal
from django.core.management.base import BaseCommand
import csv
from books.models import Book

class Command(BaseCommand):
    help = "Import books from CSV file"

    def handle(self, *args, **kwargs):
        csv_file_path = r"C:\Users\monce\OneDrive\Desktop\Django Project\expenses tracker\data\books.csv"

        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    published_date = datetime.strptime(row['published_date'], '%m/%d/%Y').date()
                except ValueError:
                    self.stdout.write(self.style.WARNING(f"Skipping invalid date: {row['published_date']}"))
                    continue  # skip this row

                book = Book(
                    title=row['title'],
                    subtitle=row.get('subtitle', ''),
                    authors=row.get('authors', 'Unknown'),
                    publisher=row['publisher'],
                    category=row['category'],
                    published_date=published_date,
                    distribution_expense=Decimal(row.get('distribution_expense', '0.00'))
                )
                book.save()

        self.stdout.write(self.style.SUCCESS('Books imported successfully!'))
