# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'employees', views.EmployeeViewSet)

urlpatterns = [
    url(
        regex=r'^$',
        view=views.IndexView.as_view(),
        name='index'
    ),
    url(r'^', include(router.urls)),
]
