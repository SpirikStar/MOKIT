# Проект Cleaning — Инструкция по запуску

## 1. Создание виртуального окружения
```bash
python -m venv .venv
```

## 2. Разрешение выполнения скриптов в PowerShell (только для Windows)
Если вы используете PowerShell и получаете ошибку выполнения, выполните:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Подробнее: [https://iqnix.link/venv](https://iqnix.link/venv)

## 3. Активация виртуального окружения
```bash
# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

## 4. Установка зависимостей
```bash
pip install django
```

## 5. Создание проекта Django
```bash
django-admin startproject cleaning .
```

## 6. Создание приложений
```bash
python manage.py startapp appModels
python manage.py startapp appRequest
```

## 7. Применение миграций
```bash
python manage.py makemigrations
python manage.py migrate
```

## 8. Создание суперпользователя
```bash
python manage.py createsuperuser
```

## 9. Запуск сервера разработки
```bash
python manage.py runserver
```

## 10. Настройка шаблонов (`templates`)
В файле `cleaning/settings.py` обновите раздел `TEMPLATES`:
```python
TEMPLATES = [
    {
        # ... остальные настройки ...
        'DIRS': [
            BASE_DIR / 'templates'
        ],
        # ...
    },
]
```

## 11. Настройка статических файлов (`static`)
В том же файле `settings.py` добавьте:
```python
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
```

## 12. Настройка маршрутов страниц

### 12.1 Представления (`views.py` в `appRequest`)
Используйте классы на основе `View` из `django.views`:
```python
from django.views import View
from django.shortcuts import render

class PersonalAccountPage(View):
    def get(self, request):
        return render(request, 'account/index.html')

...
```

### 12.2 Маршруты (`urls.py` в проекте `cleaning`)
Зарегистрируйте маршруты с обязательным слешем `/` в конце:
```python
from django.urls import path
from appRequest import views

urlpatterns = [
    path('', views.PersonalAccountPage.as_view()),# http://127.0.0.1:8000/
    path('auth/', views.AuthPage.as_view()), # http://127.0.0.1:8000/auth/
    path('reg/', views.RegPage.as_view()), # http://127.0.0.1:8000/reg/
]
```

> **Важно**: Все маршруты должны заканчиваться символом `/`, чтобы избежать редиректов и обеспечить согласованность URL.

---

## 13. Настройка прав доступа к страницам
Для обеспечения безопасности данных необходимо ограничить доступ к личному кабинету так, чтобы он был доступен только для авторизованных пользователей.

`request.user.is_authenticated`: True — пользователь авторизован; False — пользователь не авторизован.

`not`: противоположный результат.

Метод `redirect` предназначен для перенаправления пользователя на другой адрес.

```python 
class PersonalAccountPage(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('/auth/')
        return render(request, 'account/index.html')
```


Для обеспечения безопасности данных необходимо ограничить доступ к авторизации так, чтобы он был доступен только для не авторизованных пользователей.

```python 
class AuthPage(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'auth/index.html')
```

## 14. Настройка CSRF TOKEN для `<form></form>`

Для всех форм, размещённых в HTML-файлах, обязательно нужно добавить шаблонный тег `{% csrf_token %}` внутри соответствующего тега.

Пример: 
```html
<form method="POST">
    {% csrf_token %}
</form>
```
> **Важно**: без `{% csrf_token %}` Django не будет принимать данные с тега form (ошибка).


Конечно! Вот понятное и структурированное описание для **README.md**, объясняющее алгоритм авторизации в Django на основе вашего задания:

---

## 15. Алгоритм авторизации в Django

- Форма на странице авторизации отправляет данные методом **POST**.
- Если в теге `<form>` не указан атрибут `action`, данные отправляются на тот же URL, с которого была загружена страница.
- Все данные из формы (логин и пароль) доступны в представлении через `request.POST`.

15.1 **Перейдите в файл `appRequest/views.py`**  
Найдите класс `AuthPage`, отвечающий за отображение и обработку страницы авторизации.

15.2 **Добавьте метод `post`**  
Этот метод будет обрабатывать данные, отправленные через форму.

15.3 **Получите логин и пароль из запроса**:
```python
username = request.POST.get('us_login')
password = request.POST.get('us_password')
```

15.4. **Импортируйте необходимые функции** в начало файла:
```python
from django.contrib.auth import login, logout, authenticate
```

- `authenticate` — проверяет, существует ли пользователь с такими логином и паролем.
- `login` — выполняет вход (авторизацию) пользователя в системе.
- `logout` — завершает сеанс (используется при выходе, не в этом методе).

15.5. **Полная логика авторизации**:

```python
def post(self, request):
   # Получаем логин и пароль из формы
   username = request.POST.get('us_login')
   password = request.POST.get('us_password')

   # Проверяем учётные данные
   user = authenticate(request, username=username, password=password)

   # Если пользователь не найден
   if not user:
       return redirect('/auth/?error=Неверный логин или пароль')

   # Если аккаунт деактивирован
   if not user.is_active:
       return redirect('/auth/?error=Пользователь заблокирован')

   # Авторизуем пользователя
   login(request, user)

   # Перенаправляем в зависимости от прав
   if user.is_staff:
       return redirect('/admin/')  # Администраторы — в панель Django
   else:
       return redirect('/')        # Обычные пользователи — на главную
```

---
- Параметры `us_login` и `us_password` должны совпадать с атрибутами `name` в полях формы:
  ```html
  <input name="us_login" type="text">
  <input name="us_password" type="password">
  ```
- Ошибки передаются через URL-параметр `?error=...` и могут отображаться на странице `/auth/`.