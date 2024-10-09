# FILE: /product/templatetags/omfilters.py

from django.template import Library

register = Library() ##

@register.filter
def format_price(value): ##
    return f'VR${value:.2f}'.replace('.', ',') ##


# https://linktr.ee/edsoncopque