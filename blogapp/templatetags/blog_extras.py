from django import template
from django.template.defaultfilters import stringfilter
from blogapp.util import parse

register = template.Library()


@register.filter(is_safe=True)
def my_escape(value):
    return parse(value)