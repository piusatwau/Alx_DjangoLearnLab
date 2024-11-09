#Creating book

from bookshelf.models import Book

book = Book.objects.create(title="1984", author="Geaorge Orwell", publication_year="1949")
book # 1984, George Orwell, 1949