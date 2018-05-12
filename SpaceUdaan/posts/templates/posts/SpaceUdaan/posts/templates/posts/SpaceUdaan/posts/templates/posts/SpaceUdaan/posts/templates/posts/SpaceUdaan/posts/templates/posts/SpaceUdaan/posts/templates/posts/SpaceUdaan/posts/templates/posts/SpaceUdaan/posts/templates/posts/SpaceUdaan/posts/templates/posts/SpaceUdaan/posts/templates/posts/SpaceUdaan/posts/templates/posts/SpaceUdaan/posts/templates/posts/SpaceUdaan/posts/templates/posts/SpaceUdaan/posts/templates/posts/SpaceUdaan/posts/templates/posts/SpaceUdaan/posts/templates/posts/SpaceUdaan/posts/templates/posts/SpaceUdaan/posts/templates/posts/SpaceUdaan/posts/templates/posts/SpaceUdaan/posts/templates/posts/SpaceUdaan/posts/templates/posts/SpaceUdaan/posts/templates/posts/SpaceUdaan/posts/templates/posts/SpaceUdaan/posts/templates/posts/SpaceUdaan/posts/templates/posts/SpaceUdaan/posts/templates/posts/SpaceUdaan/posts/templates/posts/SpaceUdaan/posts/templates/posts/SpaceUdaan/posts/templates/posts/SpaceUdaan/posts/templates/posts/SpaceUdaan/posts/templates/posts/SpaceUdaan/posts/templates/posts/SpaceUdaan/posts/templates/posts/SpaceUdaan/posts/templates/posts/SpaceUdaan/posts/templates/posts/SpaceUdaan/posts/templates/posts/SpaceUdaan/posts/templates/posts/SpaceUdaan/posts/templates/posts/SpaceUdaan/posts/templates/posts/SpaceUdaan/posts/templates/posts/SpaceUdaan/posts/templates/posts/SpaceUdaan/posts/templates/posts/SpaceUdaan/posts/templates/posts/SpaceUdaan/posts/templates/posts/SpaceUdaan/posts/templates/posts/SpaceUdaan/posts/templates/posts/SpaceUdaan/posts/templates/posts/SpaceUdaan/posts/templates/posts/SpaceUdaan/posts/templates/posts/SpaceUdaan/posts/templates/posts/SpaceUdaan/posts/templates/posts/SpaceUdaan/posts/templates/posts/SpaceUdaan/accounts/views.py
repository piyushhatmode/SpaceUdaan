from django.shortcuts import render
from django.urls import reverse_lazy #reverse_lazy we are using usually when someone is actually logged-in or logged-out then where it actually goes
from accounts import forms
from django.views.generic import CreateView

# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy("login") #when someone has signed up for our actual webiste thn for successful sigup i will reverse them to the login page
