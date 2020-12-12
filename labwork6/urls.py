from django.contrib import admin
from django.urls import path
from django.urls import re_path
#from posts import views
from . import views


urlpatterns = [
    re_path(r'^$', views.find_start),
    re_path(r'^find_result/$', views.find_result),
    re_path(r'^course_detail/(?P<idCourse>\d+)/$', views.course_detail),
    re_path(r'^course_detail/(?P<idCourse>\d+)/course_delete/$', views.course_delete),
    re_path(r'^all_courses_delete/$', views.all_courses_delete),
    #re_path(r'^update/(?P<id>\d+)/$', views.posts_update, name='update'),
    #re_path(r'^delete/$', views.posts_delete),
    #re_path(r'^create/$', views.posts_create),
    #re_path(r'^$', views.posts_list),
]