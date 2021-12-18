from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignupForm(UserCreationForm):
    mobile = forms.IntegerField()
    email = forms.EmailField(required=True)
    # city = forms.CharField(max_length=12)
    class Meta:
        
        model = User
        fields = ['username','email','mobile']
        labels = {'mobile': 'Mobile Number'}
