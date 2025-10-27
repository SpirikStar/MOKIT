from django.contrib import admin
from appRequest import views
from django.urls import path

urlpatterns = [
    path('', views.PersonalAccountPage.as_view()),
    path('auth/', views.AuthPage.as_view()),
    path('reg/', views.RegPage.as_view()),
    path('admin/', admin.site.urls)
]
