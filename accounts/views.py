from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
#subclassing the generic class bases view CreateView in our SignUpView class
class SignUpView(generic.CreateView):
    form_class = UserCreationForm #specified the use of the built in UserCreationForm
    success_url = reverse_lazy("login") # use the reverse_lazy to redirect  the user to the login page
    template_name = "signup.html"
