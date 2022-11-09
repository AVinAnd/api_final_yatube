# api проекта yatube

В проекте описан api для сервиса yatube. 

Yatube - площадка для публикации постов, 
где пользователи могут подписываться на авторов и
оставлять комментарии.

## Как запустить проект:

Клонировать репозиторий и перейти в него в 
командной строке:

```
git clone https://github.com/AVinAnd/api_final_yatube.git
cd kittygram
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
source env/bin/activate
```
Установить зависимости из файла requirements.txt
и выполнить миграции:
```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```
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