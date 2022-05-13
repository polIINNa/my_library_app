from .models import Book
from django.forms import ModelForm, TextInput, Textarea


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['book_name', 'description']
        widgets = {
            'book_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название книги'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            })
        }

