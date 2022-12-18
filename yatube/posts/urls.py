#from django import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index),
    path('posts/', views.posts_list),
    path('group/<slug:slug>/', views.group_posts)
]