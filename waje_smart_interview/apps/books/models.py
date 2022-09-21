from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    @property
    def num_books(self):
        """
        Get the total number of books
        written by an author
        """
        return len(self.books.all())
    
class Book(models.Model):
    name = models.TextField()
    isbn = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)