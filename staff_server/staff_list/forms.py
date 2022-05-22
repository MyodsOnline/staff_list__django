from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Staff, User


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['full_name', 'job_title', 'job']


class StaffUpdateForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['full_name', 'job_title', 'job']


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
