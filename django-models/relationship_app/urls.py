from django.urls import path
from .views import BookDetailList, book_list

urlpatterns = [
    path('', book_list, name="book_list"),
    path('books/', BookDetailList.as_view(), name='book_details')
]