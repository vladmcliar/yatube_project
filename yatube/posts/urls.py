#from django import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('posts/', views.posts_list),
    path('group/', views.group_posts, name = 'group_list')
]