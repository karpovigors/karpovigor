# Приложение Друзья (Friends App)

## Описание

Это API для работы с приложением друзей. Оно позволяет пользователям отправлять, принимать, отклонять заявки в друзья, а также просматривать список друзей и удалять их.

## Установка и запуск

1. Установите зависимости: `pip install -r requirements.txt`
2. Запустите сервер: `python manage.py runserver`


## Примеры команд curl

Замените `your_token` на соответствующий токен пользователя и `127.0.0.1:8000` на адрес вашего сервера.

### Регистрация нового пользователя

curl -X POST -H "Content-Type: application/json" -d '{"username": "user1"}' http://127.0.0.1:8000/api/users/
curl -X POST -H "Content-Type: application/json" -d '{"username": "user2"}' http://127.0.0.1:8000/api/users/

### Получение токена

Для выполнения большинства запросов к API необходимо получить токен пользователя. Токен можно получить после регистрации нового пользователя, используя Shell Django:

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

user1 = User.objects.get(username='user1')
token1 = Token.objects.create(user=user1)
print(f"Token for user1: {token1}")

user2 = User.objects.get(username='user2')
token2 = Token.objects.create(user=user2)
print(f"Token for user2: {token2}")

### Выход из Shell
exit() или Ctrl+D

### Отправка заявки в друзья

curl -X POST -H "Content-Type: application/json" -H "Authorization: Token your_token_for_user1" -d '{"receiver": 2}' http://127.0.0.1:8000/api/friend-request/

### Получение списка заявок в друзья

curl -X GET -H "Authorization: Token your_token_for_user1" http://127.0.0.1:8000/api/friend-requests/

### Принятие или отклонение заявки в друзья

curl -X PUT -H "Content-Type: application/json" -H "Authorization: Token your_token_for_user2" -d '{"action": "accept"}' http://127.0.0.1:8000/api/friend-request/1/

### Просмотр списка друзей

curl -X GET -H "Authorization: Token your_token_for_user1" http://127.0.0.1:8000/api/friends/

### Получение статуса дружбы между пользователями

curl -X GET -H "Authorization: Token your_token_for_user1" http://127.0.0.1:8000/api/friendship-status/2/

### Удаление друга

curl -X DELETE -H "Authorization: Token your_token_for_user1" http://127.0.0.1:8000/api/friend-remove/2/


## Возможные ошибки и их решения

1. FieldError: Если вы столкнулись с ошибкой FieldError, убедитесь, что в коде views.py все поля модели указаны правильно. Если вы внесли изменения в модель, то выполните миграцию с помощью команды python manage.py makemigrations и python manage.py migrate.
2. Неверный URL: Если вы получаете ошибку 404 Not Found, проверьте правильность URL-адреса. Убедитесь, что вы используете правильный порт (по умолчанию 8000) и правильные адреса конечных точек.
3. Проблемы с авторизацией: Если вы получаете ошибку 401 Unauthorized, убедитесь, что вы используете правильный токен для авторизации. Если токен верный, проверьте настройки REST_FRAMEWORK в settings.py и убедитесь, что у вас включена авторизация на основе токена.
