import requests


url = "https://podolskogneupor.ru/assets/login.php"
data = {
    "fn": 'l',
    "login": "admin",
    "pass": "admin"
}
response = requests.post(url, data=data)
print(response.status_code)