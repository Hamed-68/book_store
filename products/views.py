from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Products, Book
from .forms import BookForm


class ProductsListView(ListView):
    template_name = 'products/products.html'
    model = Products


def book_view(request):
    correct_words = [
        'price', '-price', 'inventory', '-inventory',
        'created_at', '-created_at', 'name', '-name'
    ]
    template_name = 'products/books.html'
    if 'order_by' in request.GET and request.GET.get('order_by'):
        sort_key = request.GET.get('order_by')
        if sort_key in correct_words:
            books = Book.objects.all().order_by(sort_key)
            ctx = {'books': books}
            return render(request, template_name, ctx)
    books = Book.objects.all()
    ctx = {'books': books}
    return render(request, template_name, ctx)



class BookDetailView(DetailView):
    template_name = 'products/book_detail.html'
    model = Book

    def get(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        ctx = {'book': book}
        ctx['sess'] = self.request.session.keys()
        ctx['sess_key'] = self.request.session['_auth_user_id']
        ctx['cook_key'] = self.request.COOKIES.keys()

        return render(request, self.template_name, ctx)
