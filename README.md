# ELEX
### HSE Project
#### Задача проекта - электронная библиотека электронных компонентов.
##### Возможности:
* Просмотр, создание и редактирование элементов
* Регистрация и авторизация пользователей
* Различные уровни доступа. Роль "админ" позволяет просматривать логи всех участников. А так же позволяет одобрять или же отклонять заявки на добавление или удаление компонентов, производителей или их типов.
* Пользователь с ролью "админ" сможет добавлять или же удалять компонентов без прохождения модерации.
* Логирование действий пользователей
##### Особенности:
* Общение между бэкендом и фронтендом через REST API. Бэкенд не отвечает за отрисовку интерфейса, а фронтенд не хранит и не обрабатывает пользовательские данные.
* Два уровня админ панели
	1. Админ панель Django - грубая работа с моделями, а точнее, с полями базы данных. Не позволяет логировать действия пользователя. Необходима только при возникновении ситуаций, когда функционал фронтенда не будет справляться со своими задачами
	2. Админ панель Vue.js. Позволяет авторизованным пользователям вносить некоторые изменения, добавлять или новые компоненты.
##### Используемые технологии:
* Nuxt.js - фреймворк Vue.js. Готовый продукт будет представлять из себя готовый набор HTML, CSS и JS файлов и может быть размещен на любом хостинге, который поддерживает раздачу статических файлов. Основное требование - быстрый переход по страницам, отсутсвие перезагрузки страницы при добавлении/удалении/изменении компонента
* Django - бэкенд фреймворк. Хранит и обрабатывает пользовательские данные. Ведет журнал логов, который хранится в базе данных
