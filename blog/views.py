from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .location import city
from .models import *
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Post.objects.order_by('post_date')[:10]


def detail_page(request, pk, **kwargs):
    try:
        post = Post.objects.get(pk=pk)
        seen = post.seen
        seen += 1
        Post.objects.filter(pk=pk).update(seen=seen)
        context = {'post': post}
        return render(request, 'blog/detail.html', context)
    except Exception as e:
        return HttpResponse(f"{e}")


def home_page(request):
    news_list = Post.objects.filter(category=1, schedule_time__lt=timezone.now(), post_status='published')[:3]
    _city = city(request)
    lifestyle_list = []
    if Post.objects.filter(city=_city, category=2).count() > 0:
        lifestyle_list = Post.objects.filter(category=2, city=_city, schedule_time__lt=timezone.now(),
                                             post_status='published')[:3]
    else:
        lifestyle_list = Post.objects.filter(category=2, schedule_time__lt=timezone.now(), post_status='published')[:3]

    external_resources = NewsSource.objects.order_by('-created_at')[:3]
    context = {'news_list': news_list, 'lifestyle': lifestyle_list, 'news_source_list': external_resources}
    return render(request, 'blog/home.html', context)


def about_us_page(request):
    return render(request, 'blog/about_us.html')


def write_for_us_page(request):
    return render(request, 'blog/write_for_us.html')


def send_us_your_pr_page(request):
    return render(request, 'blog/send_us_your_pr.html')


def advertise_page(request):
    return render(request, 'blog/advertise.html')
