from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book, Profile
from .forms import BookForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('books')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()

                Profile.objects.create(user=user)
                messages.success(request, 'Account was created')

                return redirect('login')

        context = {'form':form}
        return render(request, 'library/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('library:books')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                print(request.user.profile.id)
                return redirect('library:books')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'library/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('library:login')

@login_required(login_url='library:login')
def books(request):
    books = Book.objects.all()
    context = {'books':books}
    return render(request, 'library/books.html', context)

@login_required(login_url='library:login')
# single book view
def bookDetail(request, pk):
    bookObj = Book.objects.get(id=pk)
    context = {'book':bookObj}
    return render(request, 'library/book-detail.html', context)
