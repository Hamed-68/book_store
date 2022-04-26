from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User, Address


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field"""

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('personal info'), {'fields': ('first_name', 'last_name', 'phone_number', 'mobile_number')}),
        (_('permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                        'groups', 'user_permissions')}),
        (_('important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'phone_number', 'mobile_number')
    search_fields = ('email', 'first_name', 'last_name', 'phone_number', 'mobile_number')
    ordering = ('email',)

admin.site.register(Address)