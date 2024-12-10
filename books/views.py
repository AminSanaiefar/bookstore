from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.urls import reverse_lazy

from .models import Book, Comment


class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    PERMISSION_NAME = 'This Page'

    def handle_no_permission(self):
        return HttpResponse(f"<h1>403 Forbidden</h1> You Dont Have Permission To <b>{self.PERMISSION_NAME}</b>!")

    def test_func(self):
        return self.request.user.is_staff


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'


def book_detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    comments = book.comments.all()
    return render(request, 'books/book_detail.html', context={'book': book, 'comments': comments})


class BookCreateView(StaffRequiredMixin, generic.CreateView):
    PERMISSION_NAME = 'Book/Create'
    model = Book
    fields = ['title', 'description', 'author', 'price', 'book_cover']
    template_name = 'books/book_create.html'
    context_object_name = 'form'


class BookUpdateView(StaffRequiredMixin, generic.UpdateView):
    PERMISSION_NAME = 'Book/Update'
    model = Book
    fields = ['title', 'description', 'author', 'price', 'book_cover']
    template_name = 'books/book_update.html'
    context_object_name = 'form'


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy("home")

