"""Scc_Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from scc import views

site_media = '/common_static/'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^scc/',include('scc.second_url')),
    #=========================================================================================
    url(r'^$',views.HomePage,name = 'home'),
    url(r'^story/',views.User_story,name = 'user_page'),#用户story界面
    url(r'^regist/',views.regist,name = 'regist'),
    url(r'^login/$',views.login,name = 'login'),#登入页面
    url(r'^uhome/$',views.uhome,name='user\'s home page'),
    url(r'^skill/$',views.skill,name='user\'s skill'),
    url(r'^userAdmin/$',views.user_admin,name='管理页面'),
    url(r'^login2/$',views.login2,name='login2'),
    url(r'^login3/$',views.login3,name='login3'),
    url(r'logout/$',views.logout),
    url(r'adminskill/$',views.Myskill_admin)
]



