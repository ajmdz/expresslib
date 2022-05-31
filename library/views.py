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
from django.db.models import Q
from .decorators import unauthenticated_user, allowed_users

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            Profile.objects.create(user=user)
            messages.success(request, 'Account was created')

            return redirect('library:login')

    context = {'form':form}
    return render(request, 'library/register.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_staff:
                return redirect('library:manage-books')
            else:
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
    
    currentUser = User.objects.get(id=request.user.id)
    my_requests = Request.objects.filter(user=currentUser, 
                                        status="PENDING").order_by('-date_created')
    my_books = Record.objects.filter(request_fk__user=request.user, returned=False).order_by('issue_date')


    search_keyword = request.GET.get('search')

    if search_keyword:
        # try:
        multiple_q = Q(
            Q(title__icontains=search_keyword) |
            Q(author__fname__icontains=search_keyword) |
            Q(author__lname__icontains=search_keyword)
        )
        books = Book.objects.filter(multiple_q)
        # except:
        #     print(search_keyword)
        #     books = None
    else:
        books = Book.objects.all().order_by('-date_added')

    context = {'books':books, 'my_requests':my_requests, 'my_books':my_books}
    return render(request, 'library/user-dashboard.html', context)

@login_required(login_url='library:login')
def bookDetail(request, pk):
    bookObj = Book.objects.get(id=pk)
    # check status: don't allow user to send duplicate requests
    try:
        inRequestTable = Request.objects.get(user=request.user, book=bookObj, status="PENDING")
    except ObjectDoesNotExist:
        print("Did not return an object")
        inRequestTable = None

    context = {'book':bookObj, 'inRequestTable': inRequestTable}
    return render(request, 'library/book-detail.html', context)

@login_required(login_url='library:login')
@allowed_users(allowed_roles=['admin'])
def adminBookDetail(request, pk):
    bookObj = Book.objects.get(id=pk)
    context = {'book':bookObj}
    return render(request, 'library/admin-book-detail.html', context)

@login_required(login_url='library:login')
@allowed_users(allowed_roles=['admin'])
def manageBooks(request):
    books = Book.objects.all()

    search_keyword = request.GET.get('search')

    if search_keyword:
        multiple_q = Q(
            Q(title__icontains=search_keyword) |
            Q(author__fname__icontains=search_keyword) |
            Q(author__lname__icontains=search_keyword)
        )
        books = Book.objects.filter(multiple_q)

    else:
        books = Book.objects.all().order_by('-date_added')

    context = {'books':books}
    return render(request, 'library/manage-books.html', context)

# book CRUD
@login_required(login_url='library:login')
@allowed_users(allowed_roles=['admin'])
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

@login_required(login_url='library:login')
@allowed_users(allowed_roles=['admin'])
def addAuthor(request):
    author_form = AuthorForm()

    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('library:add-book')

    return render(request, 'library/add-author.html', {'author_form':author_form})

@login_required(login_url='library:login')
@allowed_users(allowed_roles=['admin'])
def addPublisher(request):
    publisher_form = PublisherForm()

    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('library:add-book')

    return render(request, 'library/add-publisher.html', {'publisher_form':publisher_form})

@login_required(login_url='library:login')
@allowed_users(allowed_roles=['admin'])
def editBookDetail(request,pk):
    book = Book.objects.get(id=pk)
    form = BookForm(instance=book)

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('library:manage-books')

    context = {'form':form}
    return render(request, 'library/edit-book-detail.html', context)

@login_required(login_url='library:login')
@allowed_users(allowed_roles=['admin'])
def deleteBook(request,pk):
    book = Book.objects.get(id=pk)

    if request.method == 'POST':
        book.delete()
        return redirect('library:manage-books')

    context = {'book':book}
    return render(request, "library/confirm-delete-book.html", context)


