# Схема REST API
#### base url - http://localhost:8000/api/

#### Правила:
- Все запросы через метод POST
- Запрос строится по принципу - base url + method
        => Пример: Endpoint - token.get/, base url - http://localhost:8000/api/. Соответственно, запрос отправляется на адрес  http://localhost:8000/api/token.get/

### Endpoints:
---
## ```token.get/```
#### Первичная авторизация пользователя по логину и паролю. Проверяется разрешение пользователя на авторизацию. Возвращается объект пользователя.

### Request
|field|required|description|
|:---:|:------:|:----------|
|name|***true***|Логин пользователя|
|password|***true***|Пароль пользователя|

### Response
|field|required|description|
|:---:|:------:|:----------|
|status|***true***|***ok/fail***|
|name|***if ok***|Логин|
|isAdmin|***if ok***|Является ли пользователь админом|
|token|***if ok***|Токен доступа|
|reason|***if fail***|Причина ошибки|
|msg|***if fail***|Сообщение, которое можно показать пользователю|

---

## ```token.info/```
#### В основном, это проверка токена при инициализации приложения. Токен берется из localStorage и передается в этот эндпоинт.

### Request
|field|required|description|
|:---:|:------:|:----------|
|token|***true***|Токен пользователя|

### Response
|field|required|description|
|:---:|:------:|:----------|
|status|***true***|***ok/fail***|
|name|***if ok***|Логин|
|isAdmin|***if ok***|Является ли пользователь админом|
|token|***if ok***|Токен доступа|
|reason|***if fail***|Причина ошибки|
|msg|***if fail***|Сообщение, которое можно показать пользователю|
---

## ```token.delete/```
#### Переданный токен удаляется. Требуется для выхода из аккаунта.

### Request
|field|required|description|
|:---:|:------:|:----------|
|token|***true***|Токен пользователя|
|reason|***if fail***|Причина ошибки|
|msg|***if fail***|Сообщение, которое можно показать пользователю|

### Response
|field|required|description|
|:---:|:------:|:----------|
|status|***true***|***ok/fail***|

---

#### ```person.create/```
---

#### ```get.makers/```
---

#### ```get.types/```
---

#### ```get.elements/```
---

#### ```get.modifications/```
---

#### ```adm/get.users/```
---

#### ```adm/set.user/```

