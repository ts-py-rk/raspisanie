from django.utils.safestring import mark_safe
from django.template import Library

register = Library()

@register.filter (is_dafe=True)
def format_description(description):
    text = ''
    for i in description.split('\n'):
        # text += ('<img src="' + i + '"></img>')
        text += ( i )
        return mark_safe(text)
