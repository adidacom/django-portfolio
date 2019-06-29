from urllib.parse import quote_plus
from django import template

register = template.Library()


# Getting Django template library and register as a filter
# to use inside templates
@register.filter
def urlify(value):
    return quote_plus(value)
