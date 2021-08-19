from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.db.models import CharField, Value as V, F
from django.db.models.functions import Concat

class UserSignUpForm(UserCreactionForm):
    email = forms.EmailField

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class EmailMessageForm(forms.Form):
    #get all active registered users


    CHOICES = User.objects.all().values_list(
        #the data to be held in the value field of the dropdowns e.g. the HTML option tag 'id'

        Concat(
            F('first_name'), V(' '), F('last_name'),

            #how the data is to be displayed
            output_field=CharField()
        )   
    )
    # the drop-down to hold the registered active users (users not deleted/deactivated) fullnames and user database ids
    # the drop-down is to be populated with data from the choices variable above

    user_id = forms.ChoiceField(choices=CHOICES)

    # the email subject

    subject = forms.CharField(max_length=200)

    # the email message textarea

    message = forms.CharField(max_length=2000, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(EmailMessageForm, self).__init__(*args, **kwargs) # Call to  ModelForm constructor
        self.fields['subject'].widget.attrs['style'] = 'width:100%'
        self.fields['message'].widget.attrs['cols'] = 150
        
