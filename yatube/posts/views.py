from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def index(request):
    template = 'posts/index.html'
    return render(request, template)


def posts_list(request):
    return HttpResponse('Список постов')


# Страница со списком мороженого
def group_posts(request, slug):
    return HttpResponse(f'Список мороженого по группе{slug}')
# Create your views here.
