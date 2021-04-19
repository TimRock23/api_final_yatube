# **Yatube blog API**
API для блога [Yatube](https://github.com/TimRock23/Yatube-Blog-project). **Учебный проект**.
***

## **Описание API**
**API для сайта Yatube. Позволяет работать со следующими сущностями:**
- **Посты:**
  + Получить список всех публикаций;
  + Создать новую публикацию;
  + Получить публикацию по id;
  + Обновить публикацию по id;
  + Частично обновить публикацию по id;
  + Удалить публикацию по id.
- **Комментарии к постам:**
  + Получить список всех комментариев публикации;
  + Создать новый комментарий для публикации;
  + Получить комментарий для публикации по id;
  + Обновить комментарий для публикации по id;
  + Частично обновить комментарий для публикации по id;
  + Удалить комментарий для публикации по id.
- **JWT-токен:**
  + Получить JWT-токен;
  + Обновить JWT-токен.
- **Подписка:**
  + Получить список всех подписчиков;
  + Создать подписку;
- **Группы:**
  + Получить список всех групп;
  + Создать новую группу.
***

## **Доступные методы:**

### POSTS

`/api/v1/posts/ (GET, POST)`

`/api/v1/posts/{post_id}/ (GET, PUT, PATCH, DELETE)`

### Comments

`/api/v1/posts{post_id}/comments/ (GET, POST)`

`/api/v1/posts{post_id}/comments/{comment_id}/ (GET, PUT, PATCH, DELETE)`

### Auth

`/api/v1/auth/token/ (POST)`

`/api/v1/auth/token/refresh/ (POST)`

### Follow 

`/api/v1/follow/ (GET, POST)`


### Group

`/api/v1/group/ (GET, POST)`


## Запуск проекта (Локальный)
1. Создание виртуального окружения и подключение к нему.

`python3 -m venv venv`

`source venv/bin/activate`

2. Установка зависимостей

`pip install -r requirements.txt`

3. Развёртывание проекта

`python3 manage.py runserver`

***

## **Технологии**
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST framework](https://www.django-rest-framework.org/)
- [DRF Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
