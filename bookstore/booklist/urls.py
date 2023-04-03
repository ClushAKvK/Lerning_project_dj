from django.urls import path

from . import views

# from . import views

app_name = 'booklist'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>/>', views.index, name='index'),
    path('<int:user_id>/<int:book_id>/detail', views.detail, name='detail'),
    path('<int:user_id>/<int:book_id>/comment', views.comment, name='comment'),
    path('<int:user_id>/<int:book_id>/redirect', views.redirect, name='redirect')
]