from django.contrib import admin
from .models import Course

# Register your models here.

class CourseModelAdmin(admin.ModelAdmin):
	list_display = ['idCourse', 'nameCourse', 'urlCourse', 'descriptionCourse', 'nameUnivercity', 'timestamp']
	list_display_links = ['idCourse', 'nameCourse']
	#list_filter = ['timestamp', 'update']
	search_fields = ['idCourse', 'nameCourse']
	# list_editable = ['title']
	# inlines = [PostInstanceInline]
	# fields = ('title',)
	# exclude = ('post_likes',)


	class Meta:
		model = Course

admin.site.register(Course, CourseModelAdmin)