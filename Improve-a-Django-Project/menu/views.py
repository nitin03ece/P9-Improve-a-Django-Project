from django.shortcuts import render, get_object_or_404, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import Http404
from django.utils import timezone
from operator import attrgetter
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from . import models
from .forms import *


# Done
def menu_list(request):
    all_menus = models.Menu.objects.filter(
        Q(expiration_date__lte=timezone.now()) |
        Q(expiration_date__isnull=True)
    ).prefetch_related('items')
    return render(request, 'menu/list_all_current_menus.html', {'menus': all_menus})


def menu_detail(request, pk):
    menu = get_object_or_404(models.Menu, pk=pk)
    return render(request, 'menu/menu_detail.html', {'menu': menu})


def item_list(request):
    items = models.Item.objects.all()
    return render(request, 'menu/item_list.html', {'items':items})


def item_detail(request, pk):
    item = get_object_or_404(models.Item, pk=pk)
    return render(request, 'menu/detail_item.html', {'item': item})

@login_required
def create_new_menu(request):
    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.created_date = timezone.now()
            menu.save()
            return HttpResponseRedirect(reverse('menu:menu_detail', kwargs={'menu': menu}))
    else:
        form = MenuForm()
    return render(request, 'menu/menu_edit.html', {'form': form})


login_required
def edit_menu(request, pk):
    menu = get_object_or_404(models.Menu, pk=pk)
    items = Item.objects.all()
    if request.method == "POST":
        menu.season = request.POST.get('season', '')
        menu.expiration_date = datetime.strptime(request.POST.get('expiration_date', ''), '%m/%d/%Y')
        menu.items = request.POST.get('items', '')
        menu.save()

    return render(request, 'menu/change_menu.html', {
        'menu': menu,
        'items': items,
    })