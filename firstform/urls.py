# -*- coding:utf-8 -*-
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [

    url(r'^index/$',views.home,name='home'),
    url(r'^deployinfo/$',views.search_form),
    # url(r'^search/$',views.search),
    url(r'^sch2/$',views.deployv2),

    url(r'^cleanup/$',views.cleanup),
    url(r'^cleanaction/$',views.cleanaction),

    # 单个服务
    url(r'^singleservice/$',views.singleService,name='singleservice'),
    url(r'^installSingleService/$',views.submitSingleService),
    url(r'^dwnPkgTar/$',views.dwnPkgAndTar,name='dwnpkgtar'),

    #安装所有服务
    # url(r'^allservice/$',views.allService,name='allservice'),
    # this when access http://localhost:8000/fsp/installallservice/, this link will show the info which need to fill
    url(r'^installallservice/$', views.allService, name='allservice'),
    url(r'^submitallserviceinfo/$', views.submitallserviceinfo),


]