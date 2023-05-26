from django import template

register = template.Library()

@register.filter
def smart_floatformat(value,vvvv):
    if value is None:
        value = 0
    if vvvv is None:
        vvvv = 0

    print(value)
    print(vvvv)
    value = value+vvvv
    return value  # always return a float