from django.urls import path
from . import views as p_views

app_name = 'products'
urlpatterns = [
    path('', p_views.ProductsListView.as_view(), name='products'),
    path('books/', p_views.book_view, name='books'),
    path('books/<int:pk>/', p_views.BookDetailView.as_view(), name='book_detail'),
]
