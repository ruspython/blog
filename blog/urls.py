from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap

from blogapp.models import Post

info_dict = {
    'queryset': Post.objects.all(),
    'date_field': 'timestamp',
}

sitemaps = {
    'flatpages': FlatPageSitemap,
    'blog': GenericSitemap(info_dict, priority=0.6),
}

urlpatterns = patterns('',
                            url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt',
                                                                        content_type='text/plain')),
                            url(r'^blog/', include('blogapp.urls')),
                            url(r'^api/', include('api.urls')),
                            url(r'', include('portfolio.urls')),
                            url(r'^admin/', include(admin.site.urls)),
                            url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
                                name='django.contrib.sitemaps.views.sitemap'),
)

if settings.DEBUG:
    urlpatterns = patterns('',
                           url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                               {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    ) + staticfiles_urlpatterns() + urlpatterns