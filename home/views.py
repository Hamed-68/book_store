from django.db.models import Q
from products.models import Book
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm, AddressForm, UserProfile
from .models import User, Address
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView, UpdateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404


class UserCreateView(CreateView):
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home:home')

    def get(self, request):
        form = UserForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request):
        form = UserForm(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)
        else:
            email = form.cleaned_data.get('email')
            messages.success(request, f'{email[:email.index("@")]} عزیز، ثبت نام شما با موفقیت انجام شد!')
            form.save()
        return redirect(self.success_url)
# +++++++++++++++++++++++++++UPDATE VIEW+++++++++++++++++++++++++++++++++++

class UserUpdateView(LoginRequiredMixin, View):
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('home:home')

    def get(self, request, pk):
        if request.user.pk == pk:
            user = get_object_or_404(User, id=pk)
            if request.user.is_authenticated:
                form = UserForm(instance=user)
                addresses = Address.objects.filter(user=user.id)
                ctx = {'form': form, 'addresses': addresses}
                return render(request, self.template_name, ctx)
        else:
            raise Http404("No user matches the id.")
        return render(request, 'registration/login.html')

    def post(self, request, pk=None):
        user = get_object_or_404(User, id=pk)
        form = UserForm(request.POST, instance=user)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)
        form.save()
        return redirect(self.success_url)

# +++++++++++++++++++++++++++++ADD ANOTHER ADDRESS+++++++++++++++++++++++++++


class AddAddress(LoginRequiredMixin, CreateView):
    template_name = 'home/add_address.html'
    success_url = reverse_lazy('home:home')

    def get(self, request):
        form = AddressForm
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request):
        form = AddressForm(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)
        messages.success(request, 'آدرس جدید با موفقیت افزوده شد')
        form.instance.user = request.user
        form.save()
        return redirect(self.success_url)






#
def search(request):        # search-bar top of pages
    error = ""
    books = ""
    query = ""
    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            error = "لطفا مقدار صحیحی وارد کنید!!!"
        else:
            books = Book.objects.filter(
                Q(name__icontains=query) | Q(author__icontains=query)
            )
    else:
        error = "درخواست یافت نشد، با عرض پوزش!!!"
    context = {'error': error, 'books': books, 'query': query}
    return render(request, 'home/search_results.html', context)
