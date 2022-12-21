from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def index(request):
    template = 'posts/index.html'
    text = 'Это главная страница проекта Yatube'
    context = {
        'text': text
    }
    return render(request, template, context)


def posts_list(request):
    return HttpResponse('Список постов')


def group_posts(request):
    template = 'posts/group_list.html'
    text = 'Здесь будет информация о группах проекта Yatube'
    context = {
    'text': text
    }
    return render(request, template, context)
# Create your views here.
