from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^test/', views.test),
    url(r'^login/', views.login),
    url(r'^login_page/', views.login_page),
    url(r'^register_page/', views.register_page),
    url(r'^register/', views.register),
    url(r'^getMapDetail/', views.getMapDetail),
    url(r'^SaveMap/', views.SaveMap),
    url(r'^getAllMap/', views.getAllMap),
    url(r'^AddComment/', views.AddComment),
    url(r'^getStateDetail/', views.getStateDetail),
    url(r'^AddState/', views.AddState),
    url(r'^getHotState/', views.getHotState),
    url(r'^getNewState/', views.getNewState),
]