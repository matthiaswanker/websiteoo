"""cerandi URL Configuration

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
from cerandi_app import views
from cerandi_app.views import index_page, advisor_page, register_user,login_form

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',index_page, name="index_page" ),
    url(r'^advisor/',advisor_page, name="advisor_page"),
    url(r'^login_form', views.login_form, name="login_form"),
    url(r'^register_user/$', views.register_user, name='register_user'),
]
