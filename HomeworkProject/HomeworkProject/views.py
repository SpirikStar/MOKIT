from django.shortcuts import render
from django.views import View
from appModels import models


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')