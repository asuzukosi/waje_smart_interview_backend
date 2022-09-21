import json
from django.test import TestCase
from rest_framework.test import APIClient
from books.models import Author, Book

# Create your tests here.
class AuthorModelTest(TestCase):
    """ Test module for Author model """

    def setUp(self):
        Author.objects.create(first_name='Casper', last_name='Novest')
        Author.objects.create(first_name='Lil', last_name='Wayne')

    def test_author_name(self):
        casper_novest:Author = Author.objects.get(first_name='Casper')
        lil_wayne:Author = Author.objects.get(first_name='Lil')
        
        self.assertEqual(casper_novest.last_name, "Novest")
        self.assertEqual(lil_wayne.last_name, "Wayne")
        
        
class AuthorAPITest(TestCase):
    """ Test module for inserting a new puppy """

    def setUp(self):
        self.client = APIClient()
        Author.objects.create(first_name='Casper', last_name='Novest')
        Author.objects.create(first_name='Lil', last_name='Wayne')

    def test_get_authors(self):
        response = self.client.get("/api/authors/")
        self.assertEqual(response.status_code, 200)
        
        
    def test_create_author(self):
        body = {
            "first_name" : "Micheal", 
            "last_name": "Jackson"
        }
        response = self.client.post("/api/authors/", data=body)
        self.assertEqual(response.status_code, 201)

    
    def test_update_author(self):
         author = Author.objects.create(first_name='David', last_name='Beckam')
         body = {
             "first_name": "David",
             "last_name": "Beckham"
         }
         
         response = self.client.put(f"/api/authors/{author.id}/", data=body)
         self.assertEqual(response.status_code, 200)

class BookModelTest(TestCase):
         
    """ Test module for Book model """

    def setUp(self):
        author1 = Author.objects.create(first_name='Casper', last_name='Novest')
        author2 = Author.objects.create(first_name='Lil', last_name='Wayne')
        
        Book.objects.create(name="Flying in the winds", isbn="1223", author=author1)
        Book.objects.create(name="Into the darknes", isbn="1234", author=author2)


    def test_author_name(self):
        book1 = Book.objects.get(isbn="1223")
        book2 = Book.objects.get(isbn="1234")
        
        self.assertEqual(book1.author.first_name, "Casper")
        self.assertEqual(book1.name, "Flying in the winds")
        
        
        self.assertEqual(book2.author.first_name, "Lil")
        self.assertEqual(book2.name, "Into the darknes")