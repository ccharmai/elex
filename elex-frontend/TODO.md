#### Баги
- [ ] При перезагрузке страницы сбрасывается текущий маршрут. Это происходит потому что пользователь какое то время считается неавторизованным и перенаправляется на auth. С auth идет перенаправление на /. ***Рекомендация:*** Сделать проверку на loading авторизации и перенаправлять после загрузки.