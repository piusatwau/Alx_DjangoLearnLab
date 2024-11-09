In [1]: from bookshelf.models import Book

In [2]: book = Book.objects.create(title="1984", author= "George Orwell", publication_year=1949)

In [3]: all_books = Book.objects.all()

In [4]: print(all_books)
<QuerySet [<Book: Book object (2)>]>

In [5]: Book.objects.filter(title="1984").update(title="Nineteen Eighty-Four")
Out[5]: 1

In [6]: Book.objects.filter(title="Nineteen Eighty-Four").delete()
Out[6]: (1, {'bookshelf.Book': 1})

In [7]: