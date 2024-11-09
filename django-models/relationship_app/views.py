from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library

# Create your views here.

def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


class BookDetailList(DetailView):
    model = Library
    context_object_name = 'books'
    template_name='relationship_app/library_detail.html'