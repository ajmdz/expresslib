from django.db import models
from library.models import Book
from django.contrib.auth.models import User
# Create your models here.
class Request(models.Model):

    class RequestStatus(models.TextChoices):
        APPROVED = 'approved'
        DECLINED = 'declined'
        PENDING = 'pending'

    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, null=True, blank=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=8, choices=RequestStatus.choices, default=RequestStatus.PENDING)

# def get_expiry():
#     return datetime.today() + timedelta(days=15)
