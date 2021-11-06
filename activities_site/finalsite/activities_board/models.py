from django.db import models


class Event(models.Model):

	title = models.CharField(max_length=50, verbose_name='Название')
	content = models.TextField(null=True, blank=True, verbose_name='Описание')
	# type = models.ForeignKey('Type', null=True, on_delete=models.PROTECT, verbose_name='Категория')
	type = models.BooleanField(default=False, verbose_name='Онлайн')
	start_time = models.DateTimeField(db_index=True, verbose_name='Время начала') # присваиваем индекс, чтобы сортировать по дате проведения
	end_time = models.DateTimeField(null=True, blank=True, verbose_name='Время окончания') # не обязательно к заполнению
	location = models.TextField(null=True, blank=True, verbose_name='Место проведения')

	published = models.DateTimeField(auto_now_add=True, db_index=True,verbose_name='Время публикации')
	# автоматически вносим текущее время, присваиваем индекс, чтобы сортировать по дате публикаци
	organizer = models.ForeignKey('User', on_delete=models.PROTECT, verbose_name='Организатор')

	category = models.ManyToManyField('Category') # связи категорий с ивентами


	class Meta:
		verbose_name = 'Мероприятие'
		verbose_name_plural = 'Мероприятия'
		ordering = ['-published']

	def __str__(self):
		return self.title

class User(models.Model):

	name = models.CharField(max_length=30, verbose_name='Имя')
	surname = models.CharField(max_length=30, verbose_name='Фамилия')
	email = models.EmailField()
	password = models.CharField(max_length=30, verbose_name='Пароль')
	registrations = models.ManyToManyField(Event) # здесь будут связи пользователей с ивентами

	class Meta:
		verbose_name = 'Пользователь'
		verbose_name_plural = 'Пользователи'

	def __str__(self):
		return self.name


class Category(models.Model):

	title = models.CharField(max_length=50, verbose_name='Название')

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'

	def __str__(self):
		return self.title

class Type(models.Model):

	title = models.CharField(max_length=50, verbose_name='Название')

	class Meta:
		verbose_name = 'Тип'

class Comment(models.Model):
	event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='comments')
	name = models.CharField(max_length=80)
	body = models.TextField()
	published = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Комментарий'
		verbose_name_plural = 'Комментарии'
		ordering = ['published']