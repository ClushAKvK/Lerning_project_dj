from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from booklist.models import User


# Create your views here.

def login(request):
    users = User.objects.all()
    content = {
        'users': users
    }
    return render(request, 'authorization/login.html', content)


def redirect(request):
    user_id = request.POST['user']
    return HttpResponseRedirect(reverse('booklist:index', args=(user_id, )))