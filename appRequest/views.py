from appModels import models
from django.views import View
from django.shortcuts import render

class PersonalAccountPage(View):
    def get(self, request):
        return render(request, 'account/index.html')

class AuthPage(View):
    def get(self, request):
        return render(request, 'auth/index.html')

class RegPage(View):
    def get(self, request):
        return render(request, 'reg/index.html')