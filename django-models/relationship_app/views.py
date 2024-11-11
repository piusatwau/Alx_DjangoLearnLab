from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login

from .models import Book
from .models import Library

# Create your views here.

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', context = {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    context_object_name = 'library'
    template_name='relationship_app/library_detail.html'
    
    
# Authentification


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "relationship_app/register.html"
    
    
class SignInView(LoginView):
    form_class= AuthenticationForm
    template_name="relationship_app/login.html"
    
class SignOutView(LogoutView):
    form_class=AuthenticationForm
    template_name="relationship_app/logout.html"
    