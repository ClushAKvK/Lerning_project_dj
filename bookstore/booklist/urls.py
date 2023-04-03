from django.urls import path
from . import views

app_name = 'booklist'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_id>/detail', views.detail, name='detail')
]