from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from loducode_utils.admin import AuditAdmin

from users.models.person import Person


@admin.register(Person)
class PersonAdmin(UserAdmin, AuditAdmin):
    list_display = ('first_name', 'last_name', 'email', 'is_staff', 'rol','photo',)
    list_display_links = ('email', 'first_name', 'last_name', 'is_staff', 'rol',)
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'rol',)
    search_fields = ('email', 'first_name', 'last_name',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('personal information', {'fields': ('first_name', 'last_name', 'rol','photo')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important data', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'password1', 'password2', 'rol', 'first_name', 'last_name', 'age', 'photo', 'description',
                'phone',
                'gender')
        }),
    )
    ordering = ('email',)
