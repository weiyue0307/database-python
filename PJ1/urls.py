"""PJ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from PJ1 import views
import settings
admin.autodiscover()

urlpatterns = [
    url(r'^$',views.identity),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^myapp/', include('myapp.urls',namespace='myapp')),
    url(r'^list/$',views.select_all),
    url(r'^select/$',views.select),
    url(r'^search_form/$',views.search_form),
    url(r'^search/$',views.search),
]
