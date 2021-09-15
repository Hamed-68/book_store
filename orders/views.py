from django.shortcuts import render
from .models import Order, OrderItem
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


class OrderListView(LoginRequiredMixin, ListView): # list orders user
    template_name = 'orders/orders.html'
    model = Order

    def get_queryset(self):
        qs = Order.objects.all()
        return qs.filter(user_id = self.request.user.id)


class OrderDetailVeiw(LoginRequiredMixin, DetailView): # show all items in order
    template_name = 'orders/orders_detail.html'
    model = Order

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        order = Order.objects.get(id = self.request.user.id)
        context['orderitem_set'] = order.orderitem_set.all()
        context['total_price'] = order.total_price()
        return context


def create_order(request, pk):                  # create order or orderitem
    template_name = 'orders/create_order.html'
    obj = Order.objects.get(user_id=request.user.id)
    if obj and obj.status == False:
        past_obj_item = obj.orderitem_set.all()
        obj_item = obj.orderitem_set.create(user_id=request.user.id, product_id=pk)
        return render(request, template_name, {
            'obj': obj, 'past_obj_item': past_obj_item, 'obj_item': obj_item})
    obj = Order.objects.create(user=request.user)
    obj_item = obj.orderitem_set.create(user_id=request.user.id, product_id=pk)
    return render(request, template_name, {'obj': obj, 'obj_item': obj_item})
