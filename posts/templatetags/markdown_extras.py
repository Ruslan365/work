from django import template
from django.template.defaultfilters import stringfilter
from django import template
import calendar



import markdown as md

register = template.Library()


@register.filter()
@stringfilter
def markdown(value):
    return md.markdown(value, extensions=["markdown.extensions.fenced_code"])

register = template.Library()


@register.filter
def month_name(month_number):
    month_number = int(month_number)
    return calendar.month_abbr[month_number]