from django.db.models import Q
from django.utils import timezone
from . import models

def query():
    all_menus = models.Menu.objects.filter(
        Q(expiration_date__lte=timezone.now()) |
        Q(expiration_date__isnull=True)
    ).prefetch_related('items')
    menus = []
    for it in all_menus:
        menus.append(it)
    return menus
