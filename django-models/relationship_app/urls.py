from django.urls import path
from .views import list_books
from .views import LibraryDetailView


urlpatterns = [
    path('list/', list_books, name="book_list"),
    path('details/', LibraryDetailView.as_view(), name='book_details')
]