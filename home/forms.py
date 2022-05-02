from django import forms
from .models import Address, User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'mobile_number']

# ==================== USER PROFILE FORM ================================================
class UserProfile(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'mobile_number']

    def __init__(self, *args, **kwargs):
        super(UserProfile, self).__init__(*args, **kwargs)
        user = kwargs['instance']

        # self.fields['address'] = forms.ModelChoiceField(
        #     queryset=user.address_set, empty_label=None, label='آدرس'
        # )

# ===================== ADDRESS FORM =====================================================

AddressFormSet = forms.inlineformset_factory(User, Address, exclude=('created_at',), extra=1)