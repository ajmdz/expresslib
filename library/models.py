from django.db import models
# from django.core.validators import RegexValidator
import uuid

# Create your models here.
class Author(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    
    def __str__(self):
        return f'{self.lname}, {self.fname}'

class Publisher(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    isbn13 = models.CharField(max_length=13)
    description = models.TextField(null=True, blank=True)
    cover = models.ImageField(null=True, blank=True, default="default.jpg")
    published = models.IntegerField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title