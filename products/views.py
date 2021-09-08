from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Products, Book
from .forms import BookForm


class ProductsListView(ListView):
    template_name = 'products/products.html'
    model = Products


def book_view(request):
    template_name = 'products/books.html'
    if 'order_by' in request.GET and request.GET.get('order_by'):
        sort_key = request.GET.get('order_by')
        books = Book.objects.all().order_by(sort_key)
        ctx = {'books': books}
        return render(request, template_name, ctx)
    books = Book.objects.all()
    ctx = {'books': books}
    return render(request, template_name, ctx)



class BookDetailView(DetailView):
    template_name = 'products/book_detail.html'
    form_class = BookForm

    def get(self, request, pk):
        book = Book.objects.get(id=pk)
        ctx = {'book': book}
        return render(request, self.template_name, ctx)
