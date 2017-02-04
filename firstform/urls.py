from django.conf.urls import url
from . import views
from . import search
urlpatterns = [

    url(r'^index/',views.hello),
    url(r'^search-form/',views.search_form),
    url(r'^search/',views.search),

]