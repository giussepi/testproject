# -*- coding: utf-8 -*-
""" baseapp' urls """

from django.conf.urls import patterns, include, url
from baseapp.views import Home, LogoutView, ProfileView


urlpatterns = patterns(
    '',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^profile/$', ProfileView.as_view(), name='profile'),
)
