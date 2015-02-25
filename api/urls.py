from django.conf.urls import patterns, url

urlpatterns = patterns(
    'api.views',
    url(r'^posts/$', 'post_list', name='post_list'),
)
