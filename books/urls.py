from django.urls import path
from . import views

from .views import home, book_report

urlpatterns = [
    path('', home, name='home'),             # maps to /
    path('report/', book_report, name='book_report'),  # maps to /report/
]
