from django.shortcuts import redirect, render
from library.models import Book
from .models import Request, Record
from django.contrib.auth.models import User
# Create your views here.
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
def fetchRequests(request):
    requests = Request.objects.filter(status='PENDING').order_by('date_created')
    # for item in requests:
    #     foo = item.user.username +" "+ item.book.title
    #     print(foo)
    context = {'requests':requests}
    return render(request, 'records/admin-requests.html', context)

def approveRequest(request, pk):
    item = Request.objects.get(id=pk)
    item.status = "APPROVED"
    book = Book.objects.get(id=item.book.id)
    book.available = False
    
    if request.method == 'POST':
        item.save()
        record = Record(request=item)
        record.save()
        book.save()
        return redirect('records:borrow-requests')

    return render(request, 'records/confirm-approve.html')

def declineRequest(request, pk):
    item = Request.objects.get(id=pk)
    item.status = "DECLINED"
    
    if request.method == 'POST':
        item.save()
        return redirect('records:borrow-requests')

    return render(request, 'records/confirm-decline.html')