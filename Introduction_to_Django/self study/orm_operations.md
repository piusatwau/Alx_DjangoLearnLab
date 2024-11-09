Django’s ORM (Object-Relational Mapping) allows you to interact with your database using Python code rather than SQL. Here’s a quick guide on the basics of ORM operations in Django.

### 1. **Setting Up Models**

First, define your database tables as models in `models.py`.

```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()
```

### 2. **Creating Records**

To create records, you can either instantiate a model and call `.save()`, or use `.create()`.

```python
# Using .save()
author = Author(name="J.K. Rowling", age=55)
author.save()

# Using .create()
book = Book.objects.create(title="Harry Potter and the Sorcerer's Stone", author=author, published_date="1997-06-26")
```

### 3. **Querying Records**

Django ORM allows you to fetch data using methods like `.all()`, `.filter()`, `.get()`, and `.exclude()`.

```python
# Retrieve all records
all_authors = Author.objects.all()

# Filtering records
young_authors = Author.objects.filter(age__lt=30)

# Retrieve a single record (raises exception if multiple or no records are found)
specific_author = Author.objects.get(name="J.K. Rowling")

# Excluding records
non_hp_books = Book.objects.exclude(title__icontains="Harry Potter")
```

### 4. **Updating Records**

To update a record, first retrieve it, modify its fields, and then call `.save()`. Alternatively, you can use `.update()` on a queryset.

```python
# Update using save()
author = Author.objects.get(name="J.K. Rowling")
author.age = 56
author.save()

# Update using .update()
Author.objects.filter(name="J.K. Rowling").update(age=56)
```

### 5. **Deleting Records**

To delete records, use `.delete()`.

```python
# Delete a single record
author = Author.objects.get(name="J.K. Rowling")
author.delete()

# Delete multiple records
Author.objects.filter(age__lt=30).delete()
```

### 6. **Using Related Fields**

Django ORM makes working with related fields simple. For instance, you can access books of a specific author via reverse relationships.

```python
# Accessing related books of an author
author = Author.objects.get(name="J.K. Rowling")
books = author.book_set.all()  # or Book.objects.filter(author=author)
```

### 7. **Aggregation and Annotation**

Use aggregation functions such as `Sum`, `Avg`, `Count`, etc., to get insights into your data.

```python
from django.db.models import Count, Avg

# Count books by each author
author_book_count = Author.objects.annotate(num_books=Count('book'))

# Calculate the average age of authors
average_age = Author.objects.aggregate(Avg('age'))
```

### 8. **Ordering Results**

Use `.order_by()` to sort results.

```python
# Order authors by age, ascending
authors_by_age = Author.objects.order_by('age')

# Order authors by age, descending
authors_by_age_desc = Author.objects.order_by('-age')
```

### 9. **Bulk Operations**

For efficiency, you can create or update multiple records in bulk.

```python
# Bulk create
authors = [
    Author(name="Author 1", age=45),
    Author(name="Author 2", age=30),
]
Author.objects.bulk_create(authors)

# Bulk update
Author.objects.filter(age__lt=40).update(age=40)
```

### 10. **Transaction Management**

For complex operations, you may need to ensure all operations succeed or fail together using transactions.

```python
from django.db import transaction

try:
    with transaction.atomic():
        author = Author.objects.create(name="Author X", age=35)
        Book.objects.create(title="A New Book", author=author, published_date="2023-01-01")
except Exception as e:
    print(f"Transaction failed: {e}")
```

This should give you a solid foundation to work with Django’s ORM! L