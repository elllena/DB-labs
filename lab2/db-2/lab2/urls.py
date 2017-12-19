"""lab2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

from lab2 import views

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^main/$', views.show_main, name='main'),
    url(r'^show/$', views.show, name='show'),
    url(r'^load/$', views.load, name='load'),
    url(r'^add/$', views.add, name='add'),
    url(r'^del/$', views.delete, name='del'),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^show_date/$', views.show_date, name='show_date'),
    url(r'^show_text/$', views.show_text, name='show_text'),
    url(r'^search/$', views.search, name='search'),
    url(r'^admin/', admin.site.urls),
]
