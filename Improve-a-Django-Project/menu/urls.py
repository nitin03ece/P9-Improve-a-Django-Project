from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^(?P<pk>\d+)/edit/$', views.edit_menu, name='menu_edit'),
    url(r'^(?P<pk>\d+)/$', views.menu_detail, name='menu_detail'),
    url(r'^item/(?P<pk>\d+)/$', views.item_detail, name='item_detail'),
    url(r'^new/$', views.create_new_menu, name='menu_new'),
    url(r'^items/', views.item_list, name='item_list'),
    url(r'^$', views.menu_list, name='menu_list'),
]