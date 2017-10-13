from django.conf.urls import include, url
from django.contrib import admin
from . import views

app_name = 'users'
urlpatterns = [
    url(r'^$', views.index, name="home"),
    url(r'^addEdit/(?P<userId>[0-9]+)/$', views.addEdit, name="addEdit"),
    url(r'^(?P<userId>[0-9]+)/edit/$', views.edit, name='edit'),
    url(r'^/(?P<userId>[0-9]+)/delete/$', views.delete, name='delete')
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote')
]