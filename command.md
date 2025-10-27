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