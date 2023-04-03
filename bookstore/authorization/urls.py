from django.urls import path

from . import views

# from . import views

app_name = 'authorization'
urlpatterns = [
    path('', views.login, name='login'),
    path('redirect/', views.redirect, name='redirect')
    # path('<int:book_id>/detail', views.detail, name='detail')
]