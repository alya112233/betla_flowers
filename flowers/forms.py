from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        required=True,
        label='الاسم الأول',
        widget=forms.TextInput(attrs={
            'placeholder': 'الاسم الأول',
            'autocomplete': 'off',
        })
    )

    last_name = forms.CharField(
        max_length=30,
        required=True,
        label='اسم العائلة',
        widget=forms.TextInput(attrs={
            'placeholder': 'اسم العائلة',
            'autocomplete': 'off',
        })
    )

    email = forms.EmailField(
        required=True,
        label='البريد الإلكتروني',
        widget=forms.EmailInput(attrs={
            'placeholder': 'example@email.com',
            'autocomplete': 'off',
        })
    )

    username = forms.CharField(
        required=True,
        label='اسم المستخدم',
        widget=forms.TextInput(attrs={
            'placeholder': 'اسم المستخدم',
            'autocomplete': 'off',
        })
    )

    password1 = forms.CharField(
        label='كلمة المرور',
        widget=forms.PasswordInput(attrs={
            'placeholder': '********',
            'autocomplete': 'new-password',
        })
    )

    password2 = forms.CharField(
        label='تأكيد كلمة المرور',
        widget=forms.PasswordInput(attrs={
            'placeholder': '********',
            'autocomplete': 'new-password',
        })
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']


# ✅ نموذج استعادة كلمة المرور
class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label="البريد الإلكتروني",
        max_length=254,
        widget=forms.EmailInput(attrs={
            'autocomplete': 'email',
            'placeholder': 'example@email.com'
        })
    )
