from socket import fromshare
from django import forms
from models.customer import Customer
from django.forms import ModelForm

class CustomerForm(ModelForm):
    """
    Build the custom user form using Customer model and meta class.
    Added the password field which is not provided by default.   
    """
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = Customer
        fields = ("__all__")