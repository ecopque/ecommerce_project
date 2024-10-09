# FILE: /product/templatetags/omfilters.py

from django.template import Library
from utils import utils

register = Library() ##

@register.filter
def format_price(value): ##
    return utils.format_pricevrs(value) ##


# https://linktr.ee/edsoncopque