from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from blogapp.models import Post


class LatestPostsFeed(Feed):
    title = 'Ruspython Feed'
    link = '/sitenews/'
    description = 'Просто статейки с блога ruspython'

    def items(self):
        return Post.objects.order_by('-timestamp')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text.excerpt

