from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm


def index(request):
    books = Book.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'books': books})


def about(request):
    return render(request, 'main/about-us.html')


def add(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        form.save()
        return redirect('home')
    form = BookForm()
    context = {
        'forms': form
    }
    return render(request, 'main/add.html', context)
