from datetime import datetime
from decimal import Decimal
from django.db import models



class Book(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    authors = models.CharField(max_length=255, default="Unknown")
    publisher = models.CharField(max_length=200, default="Unknown Publisher")
    category = models.CharField(max_length=100, default="General")
    published_date = models.DateField()
    distribution_expense = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return f"{self.title} by {self.authors}"