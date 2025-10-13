from django.shortcuts import render
from django.views import View
from appModels import models


class HomeView(View):
    def get(self, request):
        us_name = request.GET.get('login')
        if not us_name:
            return render(request, 'home.html')
        
        return render(request, 'homework.html')