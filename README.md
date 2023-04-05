## Что это?

### Это пет-проект не базе Django REST Framework.
В проекте реализован API для бекенда ресурса позволяющего создавать посты, объединять их в группы, фоловить авторов и оставлять коментарии.


## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Uretzjke/api_final_yatube
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Установить djoser:

```
pip install djoser djangorestframework-simplejwt==4.7.2
```

Перейти в директорию с `manage.py`

```
cd yatube_api
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

После запуска проекта по ссылке
http://127.0.0.1:8000/redoc/
станут доступны примеры запросов и документация..
