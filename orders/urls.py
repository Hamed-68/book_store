from django.urls import path
from . import views as order_views

app_name = 'orders'
urlpatterns = [
    path('', order_views.OrderListView.as_view(), name='orders'),
    path('orders_detail/', order_views.OrderDetailVeiw.as_view(), name='orders_detail'),
    path('create_order/<int:pk>/', order_views.create_order, name='create_order'),
]
