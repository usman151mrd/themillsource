from blog.models import Menu


def menus_list(request):
    menus = Menu.objects.all()
    context = {'menus': menus}
    return context

