import pygments
from django import template
from django.utils.safestring import mark_safe
from pygments import lexers
from pygments import formatters

register = template.Library()


@register.filter(name='pygmentize', is_safe=True)
def pygmentize(value, language):
    lexer = lexers.get_lexer_by_name(language)
    output = pygments.highlight(value, lexer, formatters.HtmlFormatter(cssclass="syntax"))
    return mark_safe(output)
