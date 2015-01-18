from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
                       url(r'^$', ProjectsListView.as_view(), name='project_list'),
)
