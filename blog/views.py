from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.contrib.gis.geoip2 import GeoIP2
from .models import *


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Post.objects.order_by('post_date')[:10]


class IPTestView(generic.ListView):
    template_name = 'blog/iptest.html'
    context_object_name = 'country'

    def get_queryset(self):
        ip = get_client_ip(self.request)
        g = GeoIP2()
        response = g.country(ip)
        return response


class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'


def listing(request):
    contact_list = Post.objects.all()
    paginator = Paginator(contact_list, 25)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'list.html', {'page_obj': page_obj})
