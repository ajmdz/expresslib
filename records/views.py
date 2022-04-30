from django.shortcuts import render
from library.models import Book
from .models import Request
from django.contrib.auth.models import User
# Create your views here.
def confirmRequest(request, pk):
    user_id = User.objects.get(id=request.user.id)
    bookObj = Book.objects.get(id=pk)
    context = {'book':bookObj}
    
    newRequest = Request(user=user_id, book=bookObj)

    if request.method == 'POST':
        newRequest.save()

    return render(request, 'records/confirmRequest.html', context)