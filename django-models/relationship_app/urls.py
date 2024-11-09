from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from .views import SignUpView
from .views import SignInView
from .views import SignOutView


urlpatterns = [
    path('list/', list_books, name="book_list"),
    path('details/', LibraryDetailView.as_view(), name='book_details'),
    path('register/', SignUpView.as_view(template_name='register.html'), name="register"),
    path('login/', SignInView.as_view(template_name='logout.html'), name='login'),
    path('logout/', SignOutView.as_view(template_name='login.html'), name="logout"),
]