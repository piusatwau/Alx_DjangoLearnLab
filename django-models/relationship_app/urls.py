from django.urls import path
from .views import BookDetailList, book_list

urlpatterns = [
    path('list/', book_list, name="book_list"),
    path('details/', BookDetailList.as_view(), name='book_details')
]