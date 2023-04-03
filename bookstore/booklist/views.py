from django.shortcuts import render

from .models import Book


# Create your views here.

def index(request):
    books = Book.objects.all()
    content = {
        'books': books
    }
    return render(request, 'booklist/index.html', content)


def detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    content = {
        'book': book
    }
    return render(request, 'booklist/detail.html', content)