from django.db import models


class Event(models.Model):

	title = models.CharField(max_length=50, verbose_name='Название')
	content = models.TextField(null=True, blank=True, verbose_name='Описание')
	category = models.ForeignKey('Category', null=True, on_delete=models.PROTECT, verbose_name='Категория')
	start_time = models.DateTimeField(db_index=True, verbose_name='Время начала') # присваиваем индекс, чтобы сортировать по дате проведения
	end_time = models.DateTimeField(null=True, blank=True, verbose_name='Время окончания') # не обязательно к заполнению
	location = models.TextField(null=True, blank=True, verbose_name='Место проведения')

	published = models.DateTimeField(auto_now_add=True, db_index=True,verbose_name='Время публикации')
	# автоматически вносим текущее время, присваиваем индекс, чтобы сортировать по дате публикаци
	organizer = models.ForeignKey('User', on_delete=models.PROTECT, verbose_name='Организатор')

	# spares = models.ManyToManyField(Spare) # здесь будут связи пользователей с ивентами

	class Meta:
		verbose_name = 'Мероприятие'
		verbose_name_plural = 'Мероприятия'
		ordering = ['-published']

class User(models.Model):

	name = models.CharField(max_length=30, verbose_name='Имя')
	surename = models.CharField(max_length=30, verbose_name='Фамилия')
	email = models.EmailField()
	password = models.CharField(max_length=30, verbose_name='Пароль')

	class Meta:
		verbose_name = 'Пользователь'
		verbose_name_plural = 'Пользователи'


class Category(models.Model):

	title = models.CharField(max_length=50, verbose_name='Название')

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'


class Comment(models.Model):
	event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='comments')
	name = models.CharField(max_length=80)
	body = models.TextField()
	published = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Комментарий'
		verbose_name_plural = 'Комментарии'
		ordering = ['published']