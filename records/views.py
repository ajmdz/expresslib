from django.shortcuts import redirect, render
from .models import Request, Record
from library.models import Book
from library.decorators import allowed_users
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required(login_url='library:login')
def confirmRequest(request, pk):
    user_id = User.objects.get(id=request.user.id)
    bookObj = Book.objects.get(id=pk)
    context = {'book':bookObj}
    
    newRequest = Request(user=user_id, book=bookObj)

    if request.method == 'POST':
        newRequest.save()
        return redirect('library:book-detail', pk) # back to detail view

    return render(request, 'records/confirmRequest.html', context)

# ADMIN-ONLY VIEWS
@login_required(login_url='library:login')
@allowed_users(allowed_roles=['admin'])
def fetchRequests(request):
    requests = Request.objects.filter(status='PENDING').order_by('date_created')
    context = {'requests':requests}
    return render(request, 'records/admin-requests.html', context)

@login_required(login_url='library:login')
@allowed_users(allowed_roles=['admin'])
def fetchRecords(request):
    records = Record.objects.all().order_by('-issue_date')
    context = {'records':records}
    return render(request, 'records/admin-records.html', context)

@login_required(login_url='library:login')
@allowed_users(allowed_roles=['admin'])
def returnBook(request, pk):
    item = Record.objects.get(id=pk)
    item.returned = True
    book = Book.objects.get(id=item.request_fk.book.id)
    book.available = True

    if request.method == 'POST':
        item.save()
        book.save()
        return redirect('records:records')
        
    return render(request, 'records/confirm-return.html')

@login_required(login_url='library:login')
@allowed_users(allowed_roles=['admin'])
def approveRequest(request, pk):
    item = Request.objects.get(id=pk)
    item.status = "APPROVED"
    book = Book.objects.get(id=item.book.id)
    book.available = False
    
    if request.method == 'POST':
        item.save()
        record = Record(request_fk=item)   
        record.save()
        book.save()
        return redirect('records:borrow-requests')

    return render(request, 'records/confirm-approve.html')

@login_required(login_url='library:login')
@allowed_users(allowed_roles=['admin'])
def declineRequest(request, pk):
    item = Request.objects.get(id=pk)
    item.status = "DECLINED"
    
    if request.method == 'POST':
        item.save()
        return redirect('records:borrow-requests')

    return render(request, 'records/confirm-decline.html')