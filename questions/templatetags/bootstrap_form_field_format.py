from django import template
from django.forms import CharField, EmailField
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
def bootstrap_form_field_format(value):
    if type(value.field) in [CharField, EmailField]:
        return value.as_widget(attrs={'class': 'form-control'})
    else:
        return value
