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
from cerandi_app.views import index_page, register_user,login_form, client_list, client_detail

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',index_page, name="index_page" ),
    url(r'^client/(?P<client_pk>.*)/update/(?P<stock_pk>.*)/$',views.update_investment, name="update_investment" ),
    url(r'^client/(?P<client_pk>.*)/$',views.tinder, name="tinder" ),
    url(r'^advisor/(?P<advisor_pk>.*)/client/(?P<client_pk>.*)/analyze/$', views.analyze_page, name="analyze_page"),
    url(r'^advisor/(?P<advisor_pk>.*)/client/(?P<client_pk>.*)/$',views.client_detail, name="client_detail"),
    url(r'^advisor/(?P<advisor_pk>.*)/$',views.client_list, name="client_list"),
    url(r'^login_form', views.login_form, name="login_form"),
    url(r'^logout', views.logout, name="logout"),
    url(r'^persona_score', views.persona_score, name="persona_score"),
    url(r'^register_user/$', views.register_user, name='register_user'),
    #url(r'^client/(?P<new_Client_pk>.*)/$', views.persona_score, name='persona_score'),
]
