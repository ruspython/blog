from django.db import models
from django.template.defaultfilters import slugify

from pytils.translit import translify

from blogapp.util import unique_slugify


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        slug_str = translify(self.name)
        unique_slugify(self, slugify(slug_str))
        self.slug = slug_str
        super(Tag, self).save(*args, **kwargs)


class Project(models.Model):
    name = models.CharField(max_length=100)
    snapshot = models.ImageField(upload_to='portfolio/images')
    link = models.URLField()
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

    def get_snapshot_url(self):
        return self.snapshot.url
