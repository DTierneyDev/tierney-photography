from django import forms


class UserLoginForm(forms.Form):
    """Form used to log users in to the website"""

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
