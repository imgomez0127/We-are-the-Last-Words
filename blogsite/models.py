from django.db import models
from datetime import datetime
# Create your models here.

class Reccommended_Book(models.Model):
    book_title= models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    Book_Image = models.ImageField(blank=True, upload_to='post_imgs/')
    Buy_Link = models.CharField(max_length = 2083, blank=True)
    def __str__(self):
        return self.book_title + ' by ' + self.author

class Post(models.Model):
    Book = models.ForeignKey(Reccommended_Book, blank=True, null=True)
    title = models.CharField(max_length=50)
    date = models.DateField(default=datetime.now)
    text = models.TextField()
    Post_Image = models.ImageField(upload_to='post_imgs/', blank=True, null=True)
    credits = models.TextField(blank=True)

    def __str__(self):
        return self.title