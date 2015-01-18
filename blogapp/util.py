from html.parser import HTMLParser
from django.template.defaultfilters import urlize
import re
from django.template.defaultfilters import slugify


LT = '&lt;'
GT = '&gt;'

EXCLUDE_TAGS = ('code', 'pre', 'img', 'br', 'strong', 'b', 'i', 'em', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',)


class EscapeHTMLParser(HTMLParser):
    def __init__(self, tags=EXCLUDE_TAGS):
        HTMLParser.__init__(self)
        self.tags = tags
        self.html = []
        self.inside_code = False

    def handle_starttag(self, tag, attrs):
        if tag in self.tags:
            self.inside_code = True
            self.html.append('<%s%s>' % (tag, self.__html_attrs(attrs)))
        else:
            self.html.append(LT + '%s%s' % (tag, self.__html_attrs(attrs)) + GT)

    def handle_endtag(self, tag):
        if tag in self.tags:
            self.inside_code = False
            self.html.append('</%s>' % tag)
        else:
            self.html.append(LT + '/%s' % tag + GT)

    def handle_data(self, data):
        self.html.append(urlize(data))

    def handle_startendtag(self, tag, attrs):
        if self.inside_code and tag == 'br':
            self.html.append('\n')
        elif tag in self.tags:
            self.html.append('<%s%s/>' % (tag, self.__html_attrs(attrs)))
        else:
            self.html.append(LT + '%s%s/' % (tag, self.__html_attrs(attrs)) + GT)

    def handle_entityref(self, name):
        self.html.append('&%s;' % name)

    def handle_charref(self, name):
        self.html.append('&#%s;' % name)

    def unescape(self, s):
        return s

    def __html_attrs(self, attrs):
        _attrs = ''
        if attrs:
            _attrs = ' %s' % (' '.join([('%s="%s"' % (k, v)) for k, v in attrs]))
        return _attrs

    def feed(self, data):
        HTMLParser.feed(self, data)
        self.html = ''.join(self.html)


def parse(data):
    parser = EscapeHTMLParser()
    parser.feed(data)
    html = parser.html
    parser.close()
    return html


def unique_slugify(instance, value, slug_field_name='slug', queryset=None,
                   slug_separator='-'):
    slug_field = instance._meta.get_field(slug_field_name)

    slug = getattr(instance, slug_field.attname)
    slug_len = slug_field.max_length

    # Sort out the initial slug, limiting its length if necessary.
    slug = slugify(value)
    if slug_len:
        slug = slug[:slug_len]
    slug = _slug_strip(slug, slug_separator)
    original_slug = slug

    # Create the queryset if one wasn't explicitly provided and exclude the
    # current instance from the queryset.
    if queryset is None:
        queryset = instance.__class__._default_manager.all()
    if instance.pk:
        queryset = queryset.exclude(pk=instance.pk)

    # Find a unique slug. If one matches, at '-2' to the end and try again
    # (then '-3', etc).
    next = 2
    while not slug or queryset.filter(**{slug_field_name: slug}):
        slug = original_slug
        end = '%s%s' % (slug_separator, next)
        if slug_len and len(slug) + len(end) > slug_len:
            slug = slug[:slug_len - len(end)]
            slug = _slug_strip(slug, slug_separator)
        slug = '%s%s' % (slug, end)
        next += 1

    setattr(instance, slug_field.attname, slug)


def _slug_strip(value, separator='-'):
    """
    Cleans up a slug by removing slug separator characters that occur at the
    beginning or end of a slug.

    If an alternate separator is used, it will also replace any instances of
    the default '-' separator with the new separator.
    """
    separator = separator or ''
    if separator == '-' or not separator:
        re_sep = '-'
    else:
        re_sep = '(?:-|%s)' % re.escape(separator)
    # Remove multiple instances and if an alternate separator is provided,
    # replace the default '-' separator.
    if separator != re_sep:
        value = re.sub('%s+' % re_sep, separator, value)
    # Remove separator from the beginning and end of the slug.
    if separator:
        if separator != '-':
            re_sep = re.escape(separator)
        value = re.sub(r'^%s+|%s+$' % (re_sep, re_sep), '', value)
    return value