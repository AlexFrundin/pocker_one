from django import forms

class LoginForm(forms.Form):
    name = forms.CharField(label='Login', max_length=10)
    passwd = forms.CharField(label='Password', max_length=20, widget=forms.PasswordInput())
