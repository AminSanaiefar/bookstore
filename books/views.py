from django.views import generic
from django.urls import reverse_lazy

from .models import Book


class BookListView(generic.ListView):
    # model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.all().order_by('-id')


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'


class BookCreateView(generic.CreateView):
    model = Book
    fields = ['title', 'description', 'author', 'price']
    template_name = 'books/book_create.html'
    context_object_name = 'form'


class BookUpdateView(generic.UpdateView):
    model = Book
    fields = ['title', 'description', 'author', 'price']
    template_name = 'books/book_update.html'
    context_object_name = 'form'


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy("book_list")
