from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def status_to_css_class(status):
    if status == "debug":
        return "info"
    elif status == "info":
        return "info"
    elif status == "success":
        return "success"
    elif status == "warning":
        return "warning"
    elif status == "error":
        return "danger"
