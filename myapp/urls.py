__author__ = 'weiyue'
from django.conf.urls import url
from myapp import view,view1

urlpatterns = [
    url(r'^$', view.login,name='login'),
    url(r'^login/$',view.login,name = 'login'),
    url(r'^adminlogin/$',view.adminlogin,name='adminlogin'),
    url(r'^adminindex/$',view.adminindex,name='adminindex'),
    url(r'^search_form/$',view.search_form,name='search_form'),
    url(r'^search_choice/$',view.search_choice,name='search_choice'),
    url(r'^adminsearch_choice/$',view.adminsearch_choice,name='adminsearch_choice'),
    url(r'^search/$',view.search,name='search'),
    url(r'^regist/$',view.regist,name = 'regist'),
    url(r'^index/$',view.index,name = 'index'),
    url(r'^logout/$',view.logout,name = 'logout'),
    url(r'^dessert_search_form/$',view.dessert_search_form,name = 'dessert'),
    url(r'^dessert_shop_search_form/$',view.dessert_shop_search_form,name = 'dessert_shop'),
    url(r'^user_search_form/$',view.user_search_form,name = 'user'),
    url(r'^admindessert_search_form/$',view.admindessert_search_form,name = 'admindessert'),
    url(r'^admindessert_shop_search_form/$',view.admindessert_shop_search_form,name = 'admindessert_shop'),
    url(r'^adminuser_search_form/$',view.adminuser_search_form,name = 'adminuser'),
    url(r'^rdessert/$',view.rdessert,name = 'rdessert'),
    url(r'^rdessert_shop/$',view.rdessert_shop,name = 'rdessert_shop'),
    url(r'^ruser/$',view.ruser,name = 'ruser'),
    url(r'^shop/$',view.shop,name = 'shop'),
    url(r'^showshop/$',view.showshop,name = 'showshop'),
    url(r'^adminrdessert_shop/$',view.adminrdessert_shop,name = 'adminrdessert_shop'),
    url(r'^adminruser/$',view.adminruser,name = 'adminruser'),
    url(r'^adminrdessert/$',view.adminrdessert,name = 'adminrdessert'),


    url(r'^deleteshop/$',view1.deleteshop,name = 'deleteshop'),
    url(r'^updateshop/$',view1.updateshop,name = 'updateshop'),
    url(r'^useradd/$',view1.useradd,name = 'useradd'),
    url(r'^myself/$',view1.myself,name = 'myself'),
    url(r'^update/$',view1.update,name = 'update'),
    url(r'^addshop/$',view.addshop,name = 'addshop'),
    url(r'^delete/$',view1.delete,name = 'delete'),
    url(r'^enter/$',view1.enter,name = 'enter'),
    url(r'^userenter/$',view1.userenter,name = 'userenter'),
    url(r'^deletedessert/$',view1.deletedessert,name = 'deletedessert'),
]
