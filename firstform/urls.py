# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views
from . import search
urlpatterns = [

    url(r'^index/$',views.home,name='home'),
    url(r'^deployinfo/$',views.search_form),
    url(r'^search/$',views.search),
    url(r'^sch2/$',views.deployv2),
    url(r'^installinfo/$',views.installinfo,name='allservice'),
    url(r'^cleanup/$',views.cleanup),
    url(r'^cleanaction/$',views.cleanaction),

    # 单个服务
    url(r'^singleservice/$',views.singleService,name='singleservice'),
    url(r'^dwnPkgTar/$',views.dwnPkgTar,name='dwnpkgtar'),

    #安装所有服务
    url(r'^allservice/$',views.allService,name='allservice'),

]