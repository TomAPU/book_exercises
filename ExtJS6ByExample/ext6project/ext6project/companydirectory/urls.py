# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.IndexView.as_view(),
        name='index'
    ),
    url(r'^contactlist/$', views.EmployeeList.as_view()),
    #url(r'^tasks/(?P<pk>[0-9]+)/$', views.EmployeeDetail.as_view()),
]
