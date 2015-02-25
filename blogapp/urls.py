from django.conf.urls import patterns, include, url

from .views import *
from blog.feeds import LatestPostsFeed


urlpatterns = patterns('',
                       url(r'^feed/$', LatestPostsFeed()),
                       url(r'^tag/(?P<tag_name>[-_\w]+)/$', PostByTagListView.as_view(), name='posts_by_tag_view'),
                       url(r'^(?P<slug>[-_\w]+)/$', PostDetailView.as_view(), name='post_view'),
                       url(r'^$', PostListView.as_view()),

)
