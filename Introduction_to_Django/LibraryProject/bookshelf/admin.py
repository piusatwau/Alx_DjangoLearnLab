from django.contrib import admin
from .models import Book

# Register your models here.

# Custom display

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('publication_year')
    search_fields = ('title', 'author')
   
# this actually registers a  model in the admin panel    
admin.site.register(Book, BookAdmin)