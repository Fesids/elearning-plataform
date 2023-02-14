from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUserModel
from course.models import Course


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUserModel
        fields = UserCreationForm.Meta.fields+('email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUserModel
        fields = UserChangeForm.Meta.fields


class CourseEnrollForm(forms.Form):
    course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        widget=forms.HiddenInput
    )