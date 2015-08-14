"""ChampionProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from WaterApp import views
from WaterApp.views import index

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^CreateStudent/$', 'WaterApp.views.create_student', name='createStudent'),
    url(r'^UpdateStudent/$', 'WaterApp.views.update_student', name='updateStudent'),
    url(r'^UpdateDeleteUser/$', 'WaterApp.views.update_user', name='updateUser'),
    url(r'^CreateUser/$', 'WaterApp.views.create_user', name='createUser'),
    url(r'^CreateQuestion/$', 'WaterApp.views.create_question', name='createQuestion'),
    url(r'^UpdateQuestion/$', 'WaterApp.views.update_question', name='updateQuestion'),
    url(r'^QuestionSchedule/$', 'WaterApp.views.question_schedule', name='scheduleQuestion'),
    url(r'^AccountsManagement/$', 'WaterApp.views.accounts', name='accounts'),
    url(r'^QuestionsManagement/$', 'WaterApp.views.questions', name='questions'),
    url(r'^PerformanceManagement/$', 'WaterApp.views.bulletin', name='bulletin'),
    url(r'poll/', 'WaterApp.views.index', name='index'),
    url(r'^InvalidLogin/', 'WaterApp.views.invalid_login', name='invalidLogin'),
    url(r'^AuthorizedManagement/$', 'WaterApp.views.user_management', name='userManagement'),
    url(r'^Auth/', 'WaterApp.views.login', name="login"),
    url(r'^Logout/', 'WaterApp.views.logout', name="logout"),
    #url(r'^Auth/', 'django.contrib.auth.views.login', {'template_name': 'Main/Auth/login.html'}),
    #url(r'^Logout/', 'django.contrib.auth.views.logout', {'next_page': 'poll/Logout/logout.html'}),
    url(r'', 'WaterApp.views.index'),


]
