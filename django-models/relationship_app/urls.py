from django.urls import path
from .views import LibraryDetailView, list_books

urlpatterns = [
    path('list/', list_books, name="book_list"),
    path('details/', LibraryDetailView.as_view(), name='book_details')
]