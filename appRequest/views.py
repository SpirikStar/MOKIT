from appModels import models
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

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
    
    def post(self, request):
        username = request.POST.get('us_login')
        password = request.POST.get('us_password')

        user = authenticate(request, username=username, password=password)
        if not user:
            return redirect('/auth/?error=Неверный логин или пароль')
        
        if not user.is_active:
            return redirect('/auth/?error=Пользователь заблокирован')
        
        login(request, user)

        if user.is_staff:
            return redirect('/admin/')
        
        return redirect('/')


class RegPage(View):
    def get(self, request):
        # ! Исправить
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'reg/index.html')
    
    def post(self, request):
        us_login = request.POST.get('us_login')

        try:
            models.User.objects.get(username=us_login)
            return redirect(
                '/reg/?error=Пользователь с таким логином уже существует'
            )
        except:
            pass

        models.User.objects.create_user(
            last_name=request.POST.get('us_firstname'),
            first_name=request.POST.get('us_lastname'),
            middle_name=request.POST.get('us_middlename'),
            phone=request.POST.get('us_phone'),
            email=request.POST.get('us_email'),
            username=us_login,
            password=request.POST.get('us_password_one')
        )
        return redirect('/auth/?success=Регистрация прошла успешно')