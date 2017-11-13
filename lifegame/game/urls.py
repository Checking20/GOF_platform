from django.conf.urls import url
from . import views

urlpatterns = [
      url(r'^login/', views.login),
      url(r'^register/', views.register),
      url(r'^getState/', views.getState),
      url(r'^getMap/', views.getMap),
      url(r'^AddComment/', views.AddComment),
      url(r'^AddMap/', views.AddMap),
      url(r'^AddState/', views.AddState),
]