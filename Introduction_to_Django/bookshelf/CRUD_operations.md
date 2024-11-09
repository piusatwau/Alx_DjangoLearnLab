#Creating book

from bookshelf.models import Book

book = Book.objects.create(title="1984", author="Geaorge Orwell", publication_year="1949")
book # 1984, George Orwell, 1949


#retrieving book

book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year # 1984, George Orwell, 1949


#updating book

book = Book.objects.get(title="1984")
book.title = "Ninteen Eighty-Four"
book.save()
book.title # Nineteen Eighy-Four


Deleting book

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

retrieving all books

Book.objects.all() # nothing to show, all books deleted

