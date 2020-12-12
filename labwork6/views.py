from django.shortcuts import render
from django.http import HttpResponse

# from django.template.loader import get_template
# from django.template import Context

from django.shortcuts import get_object_or_404
# from django.core.context_processors import csrf

from .models import Course

from .forms import StartForm

from django.contrib import messages

from .courses_defs import get_courses, get_courses_add

# Create your views here.

def find_start(request):
	form = StartForm
	queryset = Course.objects.all()
	num_rec = len(queryset)
	if request.method == 'POST':
		form = StartForm(request.POST or None)
		if form.is_valid():
			new_rec = get_courses(form.cleaned_data['searchWords'])
			mess = 'Найдено {} курсов'.format(new_rec[0]) + ', ' + 'добавлено в базу {} новых курсов'.format(new_rec[1])
			messages.success(request, mess)
			queryset = Course.objects.all()
			num_rec = len(queryset)
		# else:
		# 	messages.error(request, 'Попробуйте ещё раз')
	context = {
		'form':form,
		'num_rec':num_rec,
	}
	#messages.success(request, '<a href="#">Ok</a>', extra_tags='html_safe')
	return render(request, 'find_start.html', context)


def find_result(request):
	queryset = Course.objects.all()
	num_rec = len(queryset)
	empty_lst = False
	if num_rec == 0:
		empty_lst = True
	context = {'queryset':queryset, 'title':'Сохранённые курсы', 'num_rec':num_rec, 'empty_lst':empty_lst}
	return render(request, 'index.html', context)


def course_delete(request, idCourse=None):
	if request.method == 'POST':
		instance = get_object_or_404(Course, idCourse=idCourse)
		try:
			instance.delete()
			messages.success(request, 'Курс с идентификатором {} из базы удалён'.format(idCourse))
		except Exception as e:
			err_str = 'Удаление не выполнено. Повторите ещё раз позже.' + ' ' + str(e)
			messages.error(request, err_str)
	#messages.success(request, 'Ok')
	#messages.success(request, '<a href="#">Ok</a>', extra_tags='html_safe')
	return render(request, 'course_delete.html')


def course_detail(request, idCourse=None):
	instance = get_object_or_404(Course, idCourse=idCourse)
	if instance.descriptionCourse == '' or instance.nameUnivercity == '':
		lst = get_courses_add(instance.urlCourse)
		instance.descriptionCourse = lst[0]
		instance.nameUnivercity = lst[1]
		instance.save(force_update=True)
	context = {
		'title':'Course detail',
		'instance':instance
	}
	#messages.success(request, 'Ok')
	#messages.success(request, '<a href="#">Ok</a>', extra_tags='html_safe')
	return render(request, 'course_detail.html', context)


def all_courses_delete(request):
	if request.method == 'POST':
		queryset = Course.objects.all()
		try:
			num_del = queryset.delete()[0]
			messages.success(request, 'Из бызы удалены все курсы общим числом {}'.format(num_del))
		except Exception as e:
			err_str = 'Удаление не выполнено. Повторите ещё раз позже.' + ' ' + str(e)
			messages.error(request, err_str)
	#messages.success(request, 'Ok')
	#messages.success(request, '<a href="#">Ok</a>', extra_tags='html_safe')
	return render(request, 'course_delete.html')