from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.contrib.gis.geoip2 import GeoIP2

from .forms import PRForm
from .models import *


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Post.objects.order_by('post_date')[:10]


class DetailView(generic.ListView):
    model = Post
    template_name = 'blog/detail.html'


def listing(request):
    contact_list = Post.objects.all()
    paginator = Paginator(contact_list, 25)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'list.html', {'page_obj': page_obj})


def home_page(request):
    news_list = Post.objects.filter(category=1).order_by('post_date')[:3]
    lifestyle_list = Post.objects.filter(category=2)
    external_resources = NewsSource.objects.order_by('-created_at')
    context = {'news_list': news_list, 'lifestyle': lifestyle_list, 'news_source_list': external_resources}
    return render(request, 'blog/home.html', context)


def press_form_view(request):
    return render(request, 'blog/pressform.html', {'form': PRForm()})


def about_us_page(request):
    return render(request, 'blog/about_us.html')
