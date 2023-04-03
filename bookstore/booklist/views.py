from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Book, User, Comment


# Create your views here.

def index(request, user_id=0):
    books = Book.objects.all()
    user = User.objects.get(pk=user_id)
    # print(user.id)
    content = {
        'books': books,
        'user': user
    }
    return render(request, 'booklist/index.html', content)


# def index(request, user_id):
#     books = Book.objects.all()
#     users = User.objects.all()
#     content = {
#         'books': books,
#         'users': users
#     }
#     return render(request, 'booklist/index.html', content)


def detail(request, user_id, book_id):
    book = Book.objects.get(pk=book_id)
    user = User.objects.get(pk=user_id)
    content = {
        'book': book,
        'user': user
    }
    return render(request, 'booklist/detail.html', content)


def comment(request, user_id, book_id):
    book = Book.objects.get(pk=book_id)
    user = User.objects.get(pk=user_id)
    content = {
        'book': book,
        'user': user
    }
    return render(request, 'booklist/comment.html', content)


def redirect(request, user_id, book_id):
    com = Comment(user=User.objects.get(pk=user_id), book=Book.objects.get(pk=book_id), text=request.POST['comment_text'], book_rate=request.POST['rate'])
    com.save()
    return HttpResponseRedirect(reverse('booklist:detail', args=(user_id, book_id)))