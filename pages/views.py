from django.shortcuts import render
from django.views import generic

from books.models import Book


class HomeBookListView(generic.ListView):
    # model = Book
    template_name = 'home.html'
    context_object_name = 'books'
    paginate_by = 6

    def get_queryset(self):
        return Book.objects.all().order_by('-id')
