# Как запустить проект:

## Cоздать и активировать виртуальное окружение:

###### py -m venv venv

###### source venv/scripts/activate

## Установить зависимости из файла requirements.txt:

###### py -m pip install --upgrade pip
###### pip install -r requirements.txt

## Выполнить миграции:

###### py manage.py migrate

## Запустить проект:

###### py manage.py runserver

## Примеры запросов к API

###### GET запрос на эндпоинт http://127.0.0.1:8000/api/v1/posts/ позволяет получить список публикаций
###### POST запрос на эндпоинт http://127.0.0.1:8000/api/v1/follow/ позволяет создать новую подписку
