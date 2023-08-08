from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.views import LoginView , LogoutView
from django.contrib import messages

class Login(LoginView):

    def form_valid(self, form: AuthenticationForm) -> HttpResponse:
        response =  super().form_valid(form)
        messages.success(self.request,'Login Successfull')
        return response
class Logout(LogoutView):
    pass
