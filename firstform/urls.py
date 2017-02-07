from django.conf.urls import url
from . import views
from . import search
urlpatterns = [

    url(r'^index/$',views.hello),
    url(r'^deployinfo/$',views.search_form),
    url(r'^search/$',views.search),
    url(r'^cleanup/$',views.cleanup),
    url(r'^cleanaction/$',views.cleanaction),


]