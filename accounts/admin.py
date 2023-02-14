from django.contrib import admin
from .models import CustomUserModel
from .forms import CustomUserChangeForm, CustomUserCreationForm
# Register your models here.
@admin.register(CustomUserModel)
class CustomUserAdmin(admin.ModelAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    model = CustomUserModel

    list_display = ['email', 'username', 'password', 'is_active','is_superuser']
    search_fields = ['email', 'username']