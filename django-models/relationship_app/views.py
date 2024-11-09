from django.shortcuts import render
from django.views.generic import ListView
from .models import Book
from .models import Library

# Create your views here.

def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


class BookDetailList(ListView):
    model = Library
    context_object_name = 'books'
    template_name='library_detail.html'