from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=150, default='')
    edition = models.CharField(max_length=150, default='own')
    release_date = models.DateField()
    view_amount = models.IntegerField(default=0)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.title


class User(models.Model):
    nickname = models.CharField(max_length=150, default='Incognito')
    comments_amount = models.IntegerField(default=0)

    def __str__(self):
        return self.nickname


class Comment(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, default='Incognito')
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    book_rate = models.IntegerField()

    def __str__(self):
        return self.text