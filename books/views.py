from django.shortcuts import render
from .models import Book
from django.db.models import Sum, Count

def book_report(request):
    # Get category filter from GET request
    selected_category = request.GET.get('category')

    # Filter books by selected_category if provided, else get all
    books = Book.objects.all()
    if selected_category and selected_category != 'All':
        books = books.filter(category=selected_category)

    # Get all distinct categories for dropdown
    all_categories_qs = Book.objects.values_list('category', flat=True).distinct()
    all_categories = ['All'] + sorted(all_categories_qs)

    # Aggregate counts and expenses from filtered books grouped by category
    categories_data = (
        books.values('category')
        .annotate(count=Count('id'), total_expense=Sum('distribution_expense'))
        .order_by('category')
    )

    # Prepare lists for charts
    categories = [item['category'] for item in categories_data]
    counts = [item['count'] for item in categories_data]
    expenses = [float(item['total_expense'] or 0) for item in categories_data]

    context = {
        'all_categories': all_categories,  # for dropdown filter options, including 'All'
        'categories': categories,           # categories shown on charts
        'counts': counts,                   # number of books per category (filtered)
        'expenses': expenses,               # total expense per category (filtered)
        'selected_category': selected_category or 'All',
        'books': books,                    # optionally to list filtered books
    }
    return render(request, 'books/report.html', context)


def home(request):
    return render(request, "books/home.html")
