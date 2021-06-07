# Схема REST API
#### base url - http://localhost:8000/api/

##### Правила:
- Все запросы через метод POST
- Запрос строится по принципу - base url + method
        => Пример: Endpoint - token.get/, base url - http://localhost:8000/api/. Соответственно, запрос отправляется на адрес  http://localhost:8000/api/token.get/

### Endpoints:
---
#### token.get/

##### Получаем токен для дальнейших запросов.

Request:
=> {name: name, password: password}
Параметры запроса:
- name (обязательно) - имя пользователя
- password (обязательно) - пароль пользователя

Responce:
=> {status: 'ok', name: 'Ivan', isAdmin: false, token: 'abcd...'}
=> {status: 'fail', reason: 'Invalid name or password', msg: 'Неверное имя пользователя или пароль'}

Параметры ответа:
- status (обязательно): ok или false. Успех или провал запроса.
- name (status == 'ok'): имя пользователя.
- isAdmin (status == 'ok'): является ли пользователь администратором.
- token (status == 'ok'): бессрочный токен доступа. Должен храниться как куки на фронтенде.
- reason (status == 'fail'): описание причины отказа. Как правило, это неверная пара логин/пароль
- msg (status == 'fail): сообщение, которое можно будет показать пользователю.

---
#### token.info/
##### Получение информации о токене.

Request:
=> {token: token}
Параметры запроса:
- token (обязательно) - токен доступа.

Responce:
=> {status: 'ok', name: 'Ivan', isAdmin: false}
=> {status: 'fail', reason: 'Invalid token', msg: 'Неверный токен'}

Параметры ответа:
- status (обязательно): ok или false. Успех или провал запроса
- name (status == 'ok'): имя пользователя
- isAdmin (status == 'ok'): является ли пользователь администратором
- reason (status == 'fail'): описание причины отказа. Как правило, это неверный токен.
- msg (status == 'fail): сообщение, которое можно будет показать пользователю.

---
#### person.create/
##### Создаем нового пользователя.

Request:
=> {name: name, password: password}
Параметры запроса:
- name (обязательно) - имя пользователя
- password (обязательно) - пароль пользователя

Responce:
=> {status: 'ok', name: 'Ivan', isAdmin: false, token: 'abcd...'}
=> {status: 'fail', reason: 'Name taken', msg: 'Имя пользователя занято'}

Параметры ответа:
- status (обязательно): ok или false. Успех или провал запроса
- name (status == 'ok'): имя пользователя
- isAdmin (status == 'ok'): является ли пользователь администратором
- token (status == 'ok'): бессрочный токен доступа. Необходимо сразу же запомнить его, что бы не заставлять пользователя проходить аутентификацию еще раз.
- reason (status == 'fail'): описание причины отказа. Как правило, это неверный токен.
- msg (status == 'fail): сообщение, которое можно будет показать пользователю.

---

    
