from django.urls import path
from django.views.generic import TemplateView
from . import views as home_views


app_name = 'home'
urlpatterns = [
    path('', TemplateView.as_view(template_name='home/home_page.html'), name='home'),
    path('signup/', home_views.register, name='signup'),
    path('profile/<int:pk>/', home_views.UserUpdateView.as_view(), name='profile'),
    path('search/', home_views.search, name='search'),
]
