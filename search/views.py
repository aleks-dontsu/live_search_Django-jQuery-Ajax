from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
import json

from search.models import Post


def index(request):
    posts = Post.objects.filter(is_active=True)
    context = {'posts': posts}
    return render(request, 'search/index.html', context)


def post_page(request, slug):
    post = Post.objects.get(url=slug)
    context = {'post': post}
    return render(request, 'search/post.html', context)


class PostsJson(View):
    """ Живой поиск в поисковом поле """

    def get(self, request):
        q = request.GET.get('q', '')
        post_list = []
        posts = Post.objects.filter(name__icontains=q)
        for post in posts:
            new = {'q': post.name, }
            post_list.append(new)
        return HttpResponse(json.dumps(post_list), content_type="application/json")


class JsonFilter(View):
    """ Живой фильтр постов """

    def post(self, request):
        name = request.POST.get('name')
        text = request.POST.get('text')

        posts = Post.objects.filter(is_active=True)

        if name != '':
            posts = posts.filter(name=name)
        else:
            pass
        if text != '':
            posts = posts.filter(text=text)
        else:
            pass

        queryset = posts.values(
            "url",
            "name",
            "photo",
            "text",
            "title",
        )
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = list(self.get_queryset())
        return JsonResponse({"post": queryset}, safe=False)
