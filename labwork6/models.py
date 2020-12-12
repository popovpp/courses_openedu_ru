from django.db import models

# Create your models here.

class Course(models.Model):
	id = models.AutoField(primary_key=True, verbose_name='id')
	idCourse = models.CharField(max_length=10, verbose_name='Идентификатор курса')
	nameCourse = models.CharField(max_length=120, verbose_name='Наименование курса')
	urlCourse = models.CharField(max_length=255, verbose_name='Адрес страницы курса')
	nameUnivercity = models.CharField(max_length=255, verbose_name='Название ВУЗа')
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Дата получения информации')
	descriptionCourse = models.TextField(verbose_name='Описание курса')


	def __unicode__(self):
		return self.nameCourse

	def __str__(self):
		return self.nameCourse

	def get_absolute_url(self):
		return '/courses/course_detail/{}'.format(self.idCourse)
		#return reverse('detail', kwargs={'id':self.id})


	class Meta():
		verbose_name = 'Курс'
		verbose_name_plural = 'Курсы'
		db_table = 'courses'
		ordering = ['idCourse']