
from django.conf.urls import url
from .views import show_all

urlpatterns = [

    url(r'^all$', show_all, name ='show_all'),
    url(r'^detail/<(?P<product)\d+)',detail),

]
