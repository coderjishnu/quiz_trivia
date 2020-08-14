from django.contrib import admin
from django.urls import path
from trivia_app import views

urlpatterns = [
    path("", views.index, name='index'),
    path("index", views.index, name='index'),
    path("user_Data", views.user_Data, name='user_Data'),
    path("summary", views.summary, name='summary'),
    path("history", views.history, name='history'),
]
