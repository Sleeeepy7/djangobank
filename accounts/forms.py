from django import forms
from django.core.validators import RegexValidator

from accounts.models import User, Transaction


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Телефон должен быть в формате: '+999999999'. до 15 символов разрешено.")
    phone = forms.CharField(validators=[phone_regex], max_length=17)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'phone')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class TransactionForm(forms.ModelForm):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Телефон должен быть в формате: '+999999999'. до 15 символов разрешено.")
    phone = forms.CharField(validators=[phone_regex], max_length=17)

    class Meta:
        model = Transaction
        fields = ('count', 'phone')
