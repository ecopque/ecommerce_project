# FILE: /product/templatetags/omfilter.py

from django.template import Library

register = Library() ##

def format_price(value):
    return f'R${value:.2}'

# https://linktr.ee/edsoncopque