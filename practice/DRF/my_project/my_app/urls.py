from .views import BookListCreateAPIView
from django.urls import path

urlpatterns = [
    path("api/books", BookListCreateAPIView.as_view(), name="book_list_create"),
]
