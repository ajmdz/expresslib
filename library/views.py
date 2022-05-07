from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book, Profile
from .forms import BookForm, AuthorForm, PublisherForm, CreateUserForm
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
def userDashboard(request):
    books = Book.objects.all()
    currentUser = User.objects.get(id=request.user.id)
    my_requests = Request.objects.filter(user=currentUser, 
                                        status="PENDING").order_by('-date_created')
    # fix bug: either add a user field in Record model or do complex query
    my_books = Record.objects.filter(request_fk__user=request.user, returned=False).order_by('issue_date')
    
    for book in my_books:
        print(book)
    
    context = {'books':books, 'my_requests':my_requests}
    return render(request, 'library/user-dashboard.html', context)

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

# book CRUD
def addBook(request):
    book_form = BookForm()
    author_form = AuthorForm()
    publisher_form = PublisherForm()
    

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('library:manage-books')

    context = {'book_form':book_form, 
                'author_form':author_form, 
                'publisher_form':publisher_form
                }
    return render(request, 'library/add-book.html', context)

def addAuthor(request):
    author_form = AuthorForm()

    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('library:add-book')

    return render(request, 'library/add-author.html', {'author_form':author_form})

def addPublisher(request):
    publisher_form = PublisherForm()

    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('library:add-book')

    return render(request, 'library/add-publisher.html', {'publisher_form':publisher_form})


def editBookDetail(request,pk):
    book = Book.objects.get(id=pk)
    form = BookForm(instance=book)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('library:manage-books')

    context = {'form':form}
    return render(request, 'library/edit-book-detail.html', context)

def deleteBook(request,pk):
    book = Book.objects.get(id=pk)

    if request.method == 'POST':
        book.delete()
        return redirect('library:manage-books')

    context = {'book':book}
    return render(request, "library/confirm-delete-book.html", context)


