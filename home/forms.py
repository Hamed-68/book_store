from django import forms
from .models import Address, User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'mobile_number']


class UserProfile(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        password = self.fields.get('password')
        if password:
            password.help_text = None

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'mobile_number']


class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        exclude = ('user',)
