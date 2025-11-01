from django.contrib import admin
from appRequest import views
from django.urls import path

# .as_view() - метод, который преобразует класс в представление (Запускает get или post)
urlpatterns = [
    path('', views.PersonalAccountPage.as_view()),
    path('form/', views.FormAccountPage.as_view()),
    path('auth/', views.AuthPage.as_view()),
    path('reg/', views.RegPage.as_view()),
    path('admin/', admin.site.urls)
]
