from django.shortcuts import render
from .models import Book
from django.db.models import Sum, Count
from django.http import HttpResponse

def book_report(request):
    data = (
        Book.objects
        .values('category')
        .annotate(total_expense=Sum('distribution_expense'), count=Count('id'))
        .order_by('-total_expense')
    )

    categories = [item['category'] for item in data]
    expenses = [float(item['total_expense']) for item in data]

    context = {
        'categories': categories,
        'expenses': expenses
    }

    return render(request, 'books/report.html', context)

from django.shortcuts import render

def home(request):
    return render(request, "books/home.html")