from django.urls import path
from django.views.generic import TemplateView
from . import views as home_views
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy

app_name = 'home'
urlpatterns = [
    path('', TemplateView.as_view(template_name='home/home_page.html'), name='home'),
    path('signup/', home_views.UserCreateView.as_view(), name='signup'),
    path('profile/', home_views.ProfileView.as_view(), name='profile'),
# change password
    path('password_change/',
        PasswordChangeView.as_view(template_name='registration/password_change.html',
            success_url=reverse_lazy('home:password_change_done')),
        name='password_change'),
    path('password_change/done/',
        PasswordChangeDoneView.as_view(template_name='registration/change_done.html'),
        name='password_change_done'),
# add new address
    path('add_address/', home_views.AddAddress.as_view(), name='add_address'),
#     path('search/', views.search, name='search'),
]
