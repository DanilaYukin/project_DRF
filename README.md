# DRF_Project — бэкенд для приложения курсов 

## Описание:

Приложение позволяет добавлять курсы и уроки к ним, а также оплачивать их с помощью стороннего сервиса 

## Установка:

Рекомендуется использовать PyCharm

Ссылка для добавления проекта
https://github.com/DanilaYukin/project_DRF

## Использование:

Перед началом использования создайте миграции с помощью команды python manage.py makemigrations

Далее нужно их применить с помощью команды python manage.py migrate
Для запуска используйте команду python manage.py runserver

Также можно воспользоваться Docker и собрать все в контейнеры для совместной работы с помощью Docker Compose
Для этого в терминале используйте команду 
```commandline
docker-compose up -d --build
```

Для проверки работоспособности контейнера postgres выполните команду: 
```commandline
docker exec db pg_isready -U postgres
```

Для проверки работоспособности контейнера celery выполните команду: 
```commandline
docker-compose exec celery celery -A config.celery status 
```
Также можно проверить через логи:
```commandline
docker-compose logs celery --tail=50
```

Для проверки работоспособности контейнера celery-beat выполните команду: 
```commandline
docker-compose logs celery-beat --tail=50
```

Для проверки работоспособности контейнера redis выполните команду: 
```commandline
docker-compose logs redis --tail=10
```

Для проверки работоспособности контейнера web выполните команду: 
```commandline
docker-compose logs web --tail=20
```

## Функционал

Функционал содержится в 3-ех модулях

Модули:
1. `config` - настройки проекта
2. `lms` - директория курсов и уроков
3. `users` - директория пользователей

## Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE)