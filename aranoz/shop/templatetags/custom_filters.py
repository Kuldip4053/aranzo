# yourapp/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter
def enumerate_list(value):
    """
    Takes a list and returns an enumerate object which provides index and value pairs.
    """
    return enumerate(value, start=1)  # start=1 to match the Python `enumerate` behavior
