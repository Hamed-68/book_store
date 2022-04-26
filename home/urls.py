from django.urls import path
from django.views.generic import TemplateView
from . import views as home_views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


app_name = 'home'
urlpatterns = [
    path('', TemplateView.as_view(template_name='home/home_page.html'), name='home'),
    path('signup/', home_views.UserCreateView.as_view(), name='signup'),
    path('profile/<int:pk>/', home_views.UserUpdateView.as_view(), name='profile'),
    path('add_address/', home_views.AddAddress.as_view(), name='add_address'),
    path('search/', home_views.search, name='search'),
]
