from django.shortcuts import reverse
from django.test import Client, TestCase
from django.db.models import Q
from django.utils import timezone

from .models import Menu, Item, Ingredient
from . import utility


def menu_list():
    return utility.query()


class MenuListTestCase(TestCase):
    def setUp(self):
        pass

    def test_menu_List(self):
        client = Client()
        menu = Menu.objects.filter()
        response = client.get(reverse('menu:menu_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, menu.season)
