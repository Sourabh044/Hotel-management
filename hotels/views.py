from django.shortcuts import render
from django.views import View
from django.contrib import messages

class Homepage(View):
    '''Hompage View'''
    def get(self,request,format=None):
        return render(request,'homepage.html')
