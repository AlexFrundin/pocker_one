from django.conf.urls import url
from django.views.generic import DetailView

from .models import Post
from .views import details

# urlpatterns=[
# url(r'^details/(?P<date>.+?)/(?P<slug>.+?)$', DetailView.as_view(
# model=Post,
# template_name = 'post_detail.html'
# ), name='post_details'),
# ]

urlpatterns=[
url(r'^details/(?P<date>.+?)/(?P<slug>.+?)$', details, name='post_details'),
url(r'^details/(?P<post>.+?)$', posts, name='posts'),
]
