# FILE: /product/templatetags/omfilters.py

from django.template import Library

register = Library() ##

@register.filter
def format_price(value): ##
    return f'R${value:.2}'.replace('.', ',') ##


# https://linktr.ee/edsoncopque