from django.db.models import Q
from products.models import Book
from django.shortcuts import render, redirect
from .forms import AddressFormSet, UserForm, AddressFormSet, UserProfile
from .models import User, Address
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404


def register(request):
    success_url = reverse('home:home')

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        address_form = AddressFormSet(request.POST)
        if user_form.is_valid() and address_form.is_valid():
            messages.success(request, 'Wellcom')
            user = user_form.save()
            address_form.instance = user
            address_form.save()
            return redirect(success_url)
        ctx = {'user_form': user_form, 'address_form': address_form}
        return render(request, 'registration/signup.html', ctx)
    user_form = UserForm()
    address_form = AddressFormSet()
    ctx = {'user_form': user_form, 'address_form': address_form}
    return render(request, 'registration/signup.html', ctx)
    
# +++++++++++++++++++++++++++UPDATE VIEW(profile)+++++++++++++++++++++++++++++++++++
class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('home:home')
    model = User
    form_class = UserProfile
    
    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        queryset = queryset.filter(pk=self.request.user.pk)
        try:
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404("No user matching this query")
        return obj   

    def get(self, request, *args, **kwargs):
        user_form = self.form_class(instance=self.get_object())
        address_form = AddressFormSet(instance=self.get_object())
        return render(request, self.template_name, {'user_form': user_form, 'address_form': address_form})

    def post(self, request, *args, **kwargs):
        user_form = self.form_class(request.POST, instance=self.get_object())
        address_form = AddressFormSet(request.POST, instance=self.get_object())
        if user_form.is_valid() and address_form.is_valid():
            messages.success(request, 'به روز رسانی انجام شد')
            user = user_form.save()
            address_form.user = user
            address_form.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {'user_form': user_form, 'address_form': address_form})


# search-bar
def search(request):        
    error = ""
    books = ""
    query = ""
    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            error = "لطفا مقدار صحیحی وارد کنید!!!"
        else:
            books = Book.objects.filter(
                Q(title__icontains=query) | Q(author__name__icontains=query)
            )
    else:
        error = "درخواست یافت نشد، با عرض پوزش!!!"
    context = {'error': error, 'books': books, 'query': query}
    return render(request, 'home/search_results.html', context)
