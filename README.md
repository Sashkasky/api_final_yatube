# Проект API_YAtube

# Как запустить проект:

## Cоздать и активировать виртуальное окружение:

###### python3 -m venv venv

###### source venv/scripts/activate

## Установить зависимости из файла requirements.txt:
## В проекте используются:
###### Django==2.2.16
###### pytest==6.2.4
###### pytest-pythonpath==0.7.3
###### pytest-django==4.4.0
###### djangorestframework==3.12.4
###### djangorestframework-simplejwt==4.7.2
###### Pillow==8.3.1
###### PyJWT==2.1.0
###### requests==2.26.0

###### pythonpython3 -m pip install --upgrade pip -m pip install --upgrade pip
###### pip install -r requirements.txt

## Выполнить миграции:

###### python manage.py migrate

## Запустить проект:

###### python manage.py runserver

## Примеры запросов к API

###### GET запрос на эндпоинт http://127.0.0.1:8000/api/v1/posts/ содержит список постов 
###### {
######     "count": 123,
######     "next": "http://api.example.org/accounts/?offset=400&limit=100",
######     "previous": "http://api.example.org/accounts/?offset=200&limit=100",
######     "results": [
######     + { ... }
######     ]
###### }

###### POST запрос на эндпоинт http://127.0.0.1:8000/api/v1/follow/ позволяет создать новую подписку

###### пример тела запроса:

###### {
######   "text": "string",
######   "image": "string",
######   "group": 0
###### }

###### Пример ответа:

###### {
###### "id": 0,
###### "author": "string",
###### "text": "string",
###### "pub_date": "2019-08-24T14:15:22Z",
###### "image": "string",
###### "group": 0
###### }

## Проект выполнил студент 38 когорты Александр К.
###### Github https://github.com/Sashkasky