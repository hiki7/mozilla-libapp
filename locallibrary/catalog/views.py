from django.shortcuts import render
from django.views import generic

from .models import Book, Author, BookInstance, Genre, Language

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    num_authors = Author.objects.count()

    num_languages = Language.objects.count()

    num_genres = Genre.objects.filter(name__istartswith='f').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_languages': num_languages,
        'num_genres': num_genres,
    }

    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book


class BookDetailView(generic.DetailView):
    model = Book