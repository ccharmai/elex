from django.db import models


class Person(models.Model):
	is_active = models.BooleanField(default=False, verbose_name='Активен')
	name = models.CharField(max_length=100, verbose_name='Имя')
	password = models.CharField(max_length=250, verbose_name='Хеш пароля')
	description = models.TextField(blank=True, null=True, verbose_name='Описание')
	is_admin = models.BooleanField(default=False, verbose_name='Администратор')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Пользователь'
		verbose_name_plural = 'Пользователи'


class Token(models.Model):
	person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='tokens', verbose_name='Пользователь')
	token = models.CharField(max_length=500, verbose_name='Токен')
	is_active = models.BooleanField(default=True, verbose_name='Активен')
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

	def __str__(self):
		active_msg = 'активен' if self.is_active else 'не активен'
		return f'{self.person.name} - {active_msg}'

	class Meta:
		verbose_name = 'Токен доступа'
		verbose_name_plural = 'Токены доступа'


class Maker(models.Model):
	name = models.CharField(max_length=200, verbose_name='Производитель')
	description = models.TextField(blank=True, null=True, verbose_name='Описание')
	is_visible = models.BooleanField(default=False, verbose_name='Проверен')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Производитель'
		verbose_name_plural = 'Производители'


class Type(models.Model):
	name = models.CharField(max_length=200, verbose_name='Тип')
	description = models.TextField(blank=True, null=True, verbose_name='Описание')
	is_visible = models.BooleanField(default=False, verbose_name='Проверен')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Тип'
		verbose_name_plural = 'Типы'


class Item(models.Model):
	maker = models.ForeignKey(Maker, on_delete=models.CASCADE, related_name='items', verbose_name='Предмет')
	type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='items', verbose_name='Тип')
	name = models.CharField(max_length=200, verbose_name='Название')
	is_visible = models.BooleanField(default=False, verbose_name='Проверен')

	def __str__(self):
		return f'{self.name} {self.maker.name}'

	class Meta:
		verbose_name = 'Элемент'
		verbose_name_plural = 'Элементы'


class Modification(models.Model):
	item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='items', verbose_name='Модификация')
	name = models.CharField(max_length=200, verbose_name='Название')
	is_visible = models.BooleanField(default=False, verbose_name='Проверен')

	def __str__(self):
		return self.item.name

	class Meta:
		verbose_name = 'Модификация'
		verbose_name_plural = 'Модификации'


class Property(models.Model):
	modification = models.ForeignKey(Modification, on_delete=models.CASCADE, related_name='properties', verbose_name='Модификация')
	name = models.CharField(max_length=200, verbose_name='Название')
	value = models.CharField(max_length=100, verbose_name='Значение')
	dimension = models.CharField(max_length=100, blank=True, null=True, verbose_name='Размерность')
	is_visible = models.BooleanField(default=False, verbose_name='Проверено')

	def __str__(self):
		return f'{self.modification.name} - {self.name}'

	class Meta:
		verbose_name = 'Свойство модификации'
		verbose_name_plural = 'Свойства модификации'


class Log(models.Model):
	author = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='changes', verbose_name='Пользователь')
	model = models.CharField(max_length=200, blank=True, null=True, verbose_name='Имя модели')
	comment = models.TextField(blank=True, null=True, verbose_name='Комментарий')
	time = models.DateTimeField(auto_now_add=True, verbose_name='Время')

	def __str__(self):
		return f'{self.author.name} {self.time.strftime("%d.%m.%Y %H:%M")}'

	class Meta:
		verbose_name = 'Лог'
		verbose_name_plural = 'Логи'
