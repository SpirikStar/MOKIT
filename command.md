1. Создание виртуального окружения
python -m venv .venv

2. Разрешить PowerShell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
https://iqnix.link/venv

3. Запустить виртуальное окружение
.venv/Scripts/activate 

4. Установить библиотеки
pip install django 

5. Создание проекта
django-admin startproject cleaning .

6. Создание приложения
python manage.py startapp appModels

7. Миграции
python manage.py makemigrations
python manage.py migrate

8. Создание суперпользователя
python manage.py createsuperuser

9. Запуск сервера
python manage.py runserver

10. Регистрация папки templates
Перейти в файл "settings.py"
Обновить TEMPLATES. 
TEMPLATES = [
    'DIRS': [
        BASE_DIR / 'templates'
    ],
]

11. Регистрация папки static.
Перейти в файл "settings.py". 
Создать STATICFILES_DIRS. 
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

12. Создание приложения appRequest
python manage.py startapp appRequest


13. Регистрация страниц
13.1 Перейти в views.py (находится в приложении appRequest)
13.2 Импортируйте from django.views import View (чтобы работать с ООП)
13.3 Создайте для каждой страницы свой класс. Каждый класс 
имеет метод get(). Метод get() должен обязательно возращать 
render(request, 'путь_к_файлу.html')

14. Регистрация маршрутов для страниц
14.1 Перейдите в urls.py (находится в проекте cleaning)
14.2 Каждому созданному классу задайте свой маршрут
14.2.1 http://127.0.0.1:8000/ - Личный кабинет
14.2.2 http://127.0.0.1:8000/auth/ - Авторизация
14.2.3 http://127.0.0.1:8000/reg/ - Регистрация
Важно: / -> обязательный символ после названия