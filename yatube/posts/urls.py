#from django import admin
from django.urls import include, path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name = 'home'),
    path('group/', views.group_posts, name = 'group_list'),
]