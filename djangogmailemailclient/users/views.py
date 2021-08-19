from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib import messages 
from users.forms import UserSignUpForm, EmailMessageForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'users/index.html')

def signup(request):

    if request.method == 'POST':
        # instantiate  a new form with the post data submited
        form = UserSignUpForm(request.POST)

        if form.is_valid():
            # call the form.save() method to save the data to the DB
            form.save()
            messages.success(request, f'Your account has been created')
            return redirect('login')
    # pass a blank sign up form when a user navigates to this page through a GET request
    else:
        form = UserSignUpForm()
    return render(request, 'users/signup.html', {'form': form})


@login_reqired
def send_email(request):
    if request.method == "POST":
        # instantiate a new form with the data submitted
        form = EmailMessageForm(request.POST)
        if form.is_valid():

            #get the submitted subject
            subject = form.cleaned_data['subject']

            # get the submitted message
            message = form.cleaned_data['message']

            # get the submitted user_id which is the value of the option that was selected and submitted
            user_id = form.cleaned_data['user_id']

            # get the user associated with the passed used_id
            user = User.objects.get(user_id)


            user.email_user(subject, message, request.user.get_full_name(), fail_silently=True)

            messages.success(request, f'An email has been sent to {user.get_full_name()}')

            return redirect('index')

    # pass the blan email message form when a user navigates to the email page through a GET request

    else:
        form = EmailMessageForm()

        context = {'form': form}

        return render(request, 'users/send_email.html', context)


