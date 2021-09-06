from django import forms
from .models import UserAddress, User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class UserForm(UserCreationForm):
    password1 = forms.CharField(max_length=200, label='رمز',
        widget=forms.PasswordInput(), help_text='رمز باید شامل حروف و عدد باشد')
    password2 = forms.CharField(max_length=200, label='تکرار رمز',
        widget=forms.PasswordInput(), help_text='')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email',
            'address']

        labels = {'first_name': 'نام', 'last_name': 'نام خانوادگی',
            'username': 'نام کاربری', 'email': 'ایمیل', 'address': 'آدرس'}

        help_texts = {
        'username': 'کمتر از 150 کاراکتر که فقط میتواند شامل حروف/عدد/@/ ./ -/ _ /+ باشد'
        }


class UserProfile(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        password = self.fields.get('password')
        if password:
            password.help_text = None

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'address']
        labels = {'first_name': 'نام', 'last_name': 'نام خانوادگی',
            'username': 'نام کاربری', 'email': 'ایمیل', 'address': 'آدرس'}


class UserAddressForm(forms.ModelForm):

    class Meta:
        model = UserAddress
        fields = ['name']
        labels = {'name': 'آدرس'}
        help_texts = {'name': 'لطفا آدرس را کامل وارد کنید!'}
