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
    url(r'^tasks/$', views.TodoList.as_view()),
    url(r'^tasks/(?P<pk>[0-9]+)/$', views.TodoDetail.as_view()),
]
