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

#SOLUTION 2

# Query all books by a specific author
author_name = 'Specific Author Name'  # Replace with the actual author's name
try:
    author = Author.objects.get(name=author_name)
    author_books = Book.objects.filter(author=author)
    print(f"Books by {author_name}:")
    for book in author_books:
        print(book.title)
except Author.DoesNotExist:
    print(f"Author with name '{author_name}' does not exist.")

# List all books in a specific library
library_name = 'Specific Library Name'  # Replace with the actual library name
try:
    library = Library.objects.get(name=library_name)
    library_books = library.books.all()
    print(f"Books in {library_name}:")
    for book in library_books:
        print(book.title)
except Library.DoesNotExist:
    print(f"Library with name '{library_name}' does not exist.")

# Retrieve the librarian for a specific library
try:
    librarian = library.librarian  # Access the related librarian
    print(f"Librarian of {library_name}: {librarian.name}")
except Library.DoesNotExist:
    print(f"Library with name '{library_name}' does not exist.")
except Librarian.DoesNotExist:
    print(f"Librarian for '{library_name}' does not exist.")
