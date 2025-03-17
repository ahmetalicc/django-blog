from django.contrib import admin
from account.models import CustomUserModel
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUserModel
    list_display = ("username", "email")
    fieldsets = UserAdmin.fieldsets + (
        (
            'Avatar change', {
                'fields' : ['avatar']
            }
        ),
    )

admin.site.register(CustomUserModel, CustomUserAdmin)