from .models import Book, Librarian, Library

#Query all books by a specific author.
Book.objects.get(author="")

# List all books in a library.
Library.objects.all()

# Retrieve the librarian for a library.
Librarian.objects.get(library="")