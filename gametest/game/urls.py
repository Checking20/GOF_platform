from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^share/', views.share),
    url(r'^begin/', views.begin),
    url(r'^work/', views.work),
    url(r'^login/', views.login),
    url(r'^register/', views.register),
    url(r'^getMapDetail/', views.getMapDetail),
    url(r'^AddMap/', views.AddMap),
    url(r'^getAllMap/', views.getAllMap),
    url(r'^AddComment/', views.AddComment),
    url(r'^getStateDetail/', views.getStateDetail),
    url(r'^AddState/', views.AddState),
    url(r'^getHotState/', views.getHotState),
    url(r'^getNewState/', views.getNewState),
    url(r'^AddLike/', views.AddLike),
]