from django.db import models
from library.models import Book
from django.contrib.auth.models import User
from datetime import datetime, timedelta
# Create your models here.
class Request(models.Model):

    class RequestStatus(models.TextChoices):
        APPROVED = 'APPROVED'
        DECLINED = 'DECLINED'
        PENDING = 'PENDING'

    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, null=True, blank=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=8, choices=RequestStatus.choices, default=RequestStatus.PENDING)
    def __str__(self):
        return str(self.book) + " - " + str(self.user) 

class Record(models.Model):
    class BorrowStatus(models.TextChoices):
        ONGOING = 'ONGOING'
        RETURNED = 'RETURNED'
        OVERDUE = 'OVERDUE'

    def get_returnDate():
        return datetime.today() + timedelta(days=7)

    request = models.ForeignKey(Request, null=True, blank=True, on_delete=models.CASCADE)
    issue_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(default=get_returnDate)
    status = models.CharField(max_length=8, choices=BorrowStatus.choices, default=BorrowStatus.ONGOING)
    # fine = models.DecimalField(default=0, decimal_places=2, max_digits=7)
    
    def __str__(self):
        return str(self.status) + " - " + str(self.request)

