from django.db import models
from library.models import Book
from django.contrib.auth.models import User
# Create your models here.
class Request(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, null=True, blank=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    # add enum field for status

# def get_expiry():
#     return datetime.today() + timedelta(days=15)
