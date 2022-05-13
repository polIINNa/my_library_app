from django.db import models


class Book(models.Model):
    book_name = models.CharField('Название книги', max_length=50)
    description = models.TextField('Описание книги')

    def __str__(self):
        return self.book_name
