# Проект API_YAtube

# Как запустить проект:

## Технические требования к компьютеру:
###### Windows версии 7 или 10, Apple macOS, Linux Ubuntu 18.04 (Bionic Beaver) или 20.04 (Focal Fossa).
###### Компьютер: минимум 4 Гб оперативной памяти.

###### Инструкция для Windows
###### Установите программное обеспечение: скачайте установочные файлы и запустите их.
###### Python: www.python.org/downloads/
###### Visual Studio Code: code.visualstudio.com/download
###### Git: git-scm.com/download/win

###### Инструкция для macOS
###### Первым делом установим утилиты разработчика, после этого — менеджер пакетов Homebrew https://brew.sh/, а потом, уже через HomeBrew, установим все остальные программы.
###### Запустите программу Терминал (или Terminal.app), она находится в директории /Applications/Utilities/. Все команды будем выполнять в окне этой программы.

###### Инструкция для Linux (Ubuntu)
###### Запустите программу Терминал.
###### Сперва установите Python, для этого в терминале выполните команду
###### sudo apt-get install python3.7 
###### Перед установкой терминал попросит вас ввести пароль администратора — сделайте это.
###### По такой же схеме установите Git
###### sudo apt-get install git 
###### Чтобы установить редактор вам понадобится менеджер пакетов snap. Установите его командой
###### sudo apt install snap 
###### Устанавливаем редактор Visual Studio Code из дополнительного набора пакетов:
###### sudo snap install code --classic 
###### После того, как всё скачается и установится, вы сможете запустить Visual Studio Code командой code в терминале.

## Cоздать и активировать виртуальное окружение:

###### python3 -m venv venv для юникс систем
###### python -m venv venv для ос windows

###### source venv/scripts/activate

## Установить зависимости из файла requirements.txt:

###### pythonpython3 -m pip install --upgrade pip -m pip install --upgrade pip
###### pip install -r requirements.txt

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

## Выполнить миграции:

###### python manage.py migrate

## Запустить проект:

###### python manage.py runserver

## Примеры запросов к API

###### GET запрос на эндпоинт http://127.0.0.1:8000/api/v1/posts/ Получить список всех публикаций. При указании параметров limit и offset выдача должна работать с пагинацией. 
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