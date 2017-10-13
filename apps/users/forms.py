from django import forms

class UserForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email_address = forms.CharField(label='Email Address', max_length=100)
    