from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import employeebiodata.forms

import employeebiodata.views
from employeebiodata import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/', views.list, name='list'),
    url(r'^add/', views.add, name='add')

]