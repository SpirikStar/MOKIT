from appModels import models
from django.views import View
from django.shortcuts import render, redirect

class PersonalAccountPage(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('/auth/')
        return render(request, 'account/index.html')

class AuthPage(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'auth/index.html')

class RegPage(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'reg/index.html')