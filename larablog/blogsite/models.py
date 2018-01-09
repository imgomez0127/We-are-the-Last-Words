from django.db import models
from datetime import datetime
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField(default=datetime.now())
    text = models.TextField()
    Post_Image = models.ImageField(blank=True,upload_to='post_imgs/')
    def __str__(self):
        return self.title
class BookPost(Post):
    book_title = models.CharField(max_length=50)
    genre = models.CharField(max_length=20)

class ReccommendedBooks(models.Model):
    book_title= models.CharField(max_length=50)
    genre = models.CharField(max_length=20)
