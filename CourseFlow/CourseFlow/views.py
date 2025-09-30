from django.shortcuts import render
from django.views import View
from appModels.models import *


class PageHome(View):
    def get(self, request):
        return render(request, 'home.html')
