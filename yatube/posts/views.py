from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse('Главная страница')


def posts_list(request):
    return HttpResponse('Список постов')


# Страница со списком мороженого
def group_posts(request, slug):
    return HttpResponse(f'Список мороженого по группе{slug}')
# Create your views here.
