from django.db import models


class Person(models.Model):
	name = models.CharField(max_length=100)
	password = models.CharField(max_length=250)
	description = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.name


class Maker(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.name


class Type(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.name


class Item(models.Model):
	maker =models.ForeignKey(Maker, on_delete=models.CASCADE, related_name='items')
	type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='items')
	name = models.CharField(max_length=200)

	def __str__(self):
		return f'{self.name} {self.maker.name}'


class Modification(models.Model):
	item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='items')

	def __str__(self):
		return self.item.name


class Property(models.Model):
	modification = models.ForeignKey(Modification, on_delete=models.CASCADE, related_name='properties')
	name = models.CharField(max_length=200)
	value = models.CharField(max_length=100)
	dimension = models.CharField(max_length=100, blank=True, null=True)

	def __str__(self):
		return f'{self.modification.name} - {self.name}'


class Log(models.Model):
	author = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='changes')
	model = models.CharField(max_length=200, blank=True, null=True)
	comment = models.TextField(blank=True, null=True)
	time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.author.name} {self.time.strftime("%d.%m.%Y %H:%M")}'
