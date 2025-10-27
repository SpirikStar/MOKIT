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