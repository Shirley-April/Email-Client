from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.db.models import CharField, Value as V, F
from django.db.models.functions import Concat

class UserSignUpForm(UserCreactionForm):
    email = forms.EmailField

    class Meta:
        