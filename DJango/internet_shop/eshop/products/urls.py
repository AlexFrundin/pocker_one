
from django.conf.urls import url
from .views import show_all, detail
from django.views.generic import ListView
from .models import Product

urlpatterns = [
    url(r'^$', show_all, name='show_all'),
    url(r'^all/$', show_all, name ='show_all'),
    #url(r'^all0/$',ListView.as_view(
    #model=Product, paginate_by=2, template_name='show_all0.html')),
    url(r'^detail/(?P<product_id>\d+)$', detail, name='detail')

]
