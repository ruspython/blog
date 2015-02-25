from datetime import timezone
from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify

from pytils.translit import translify
from model_utils.fields import SplitField

from portfolio.models import Tag
from blogapp.util import unique_slugify


class Post(models.Model):
    title = models.CharField(max_length=150)
    tags = models.ManyToManyField(Tag)
    slug = models.SlugField(max_length=150, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    text = SplitField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        slug_str = translify(self.title)
        unique_slugify(self, slug_str)
        self.slug = slugify(slug_str)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post_view', args=[str(self.slug)])

    def get_context_data(self, **kwargs):
        context = super(Post, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    def get_tags(self):
        return self.tags.all()