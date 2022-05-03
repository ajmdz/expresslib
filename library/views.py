from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book, Profile
from .forms import BookForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from records.models import Request, Record
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('library:books')
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
def bookDetail(request, pk):
    bookObj = Book.objects.get(id=pk)
    # check status: don't allow user to send duplicate requests
    """
        Possible bug: if book status is not reset to available
            after approval and return.
        So, set the status back to available after the book is returned 
    """
    try:
        inRequestTable = Request.objects.get(user=request.user, book=bookObj, status="PENDING")
    except ObjectDoesNotExist:
        print("Did not return an object")
        inRequestTable = None

    context = {'book':bookObj, 'inRequestTable': inRequestTable}
    return render(request, 'library/book-detail.html', context)

def manageBooks(request):
    books = Book.objects.all()
    context = {'books':books}
    return render(request, 'library/manage-books.html', context)