from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author (replace 'author_name' with the actual name)
author_name = 'Specific Author Name'
author_books = Book.objects.filter(author__name=author_name)
print(f"Books by {author_name}:")
for book in author_books:
    print(book.title)

# List all books in a library (replace 'library_name' with the actual name)
library_name = 'Specific Library Name'
library = Library.objects.get(name=library_name)
library_books = library.books.all()
print(f"Books in {library_name}:")
for book in library_books:
    print(book.title)

# Retrieve the librarian for a library (replace 'library_name' with the actual name)
library = Library.objects.get(name=library_name)
librarian = library.librarian  # Access the related librarian
print(f"Librarian of {library_name}: {librarian.name}")
