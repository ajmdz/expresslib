from django import forms
from django.forms import ModelForm
from .models import Book
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title','author','isbn13',
                    'description', 'cover', 
                    'published', 'publisher',
                    'available', ]

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']