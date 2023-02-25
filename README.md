# API проекта yatube

В проекте описан API для сервиса yatube. 

Yatube - площадка для публикации постов, 
где пользователи могут подписываться на авторов и
оставлять комментарии.

## Технологии и запуск проекта

Проект написан на языке python, с использованием django REST framework. 
Необходимые для работы проекта зависимости описаны в файле requirements.txt
### Технологии проекта:
- Python 3.7
- Django Rest Framework
- Simple JWT
- Djoser

Документация проекта доступна по адресу 
http://127.0.0.1:8000/redoc/

Для запуска проекта:
- Клонируйте репозиторий
``` 
- git clone https://github.com/AVinAnd/api_final_yatube.git 
```
- Активируйте виртуальное окружение 
```
python -m venv venv
source venv/scripts/activate
```
- Установите зависимости
``` 
pip install -r requirements.txt
```
- Выполните миграции 
```
python manage.py makemigrations
python manage.py migrate
```
- Запустите проект
```
python manage.py runserver
```

Проект доступен по адресу http://127.0.0.1:8000/
## Примеры запросов
### GET запросы
```
/api/v1/posts/ - получение публикаций
/api/v1/posts/{id}/ - получение публикации
/api/v1/posts/{id}/comments - получение комментариев
/api/v1/posts/{id}/comments/{id} - получение комментария
/api/v1/groups/ - список сообществ
/api/v1/groups/{id}/ - информация о сообществе
/api/v1/follow/ - подписки
```
### POST запросы
```
/api/v1/posts/ - создание публикации
    {
        "text": "string",
    }
    
/api/v1/posts/{id}/comments - создание комментария
    {
        "text": "string"
    }

/api/v1/follow/ - подписка на автора
    {
        "following": "string"
    }
```
## Об авторе
Андрей Виноградов - студент Яндекс Практикум
по курсу Python-разработчик
