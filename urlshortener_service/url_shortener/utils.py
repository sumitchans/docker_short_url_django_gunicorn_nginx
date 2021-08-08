import os

from django.conf import settings
import string

from .models import Shortener


MIN_LENGTH = getattr(settings, "MIN_LENGTH")


def get_unique_id(num, base=62, min_length=MIN_LENGTH):
    """
    Function to get unique string
    """
    result = ""
    alphabet = string.ascii_letters + string.digits
    while num > 0:
        remainder = num % base
        result = result + alphabet[remainder]
        num = num // base
    padding = alphabet[0] * (min_length - len(result))
    return result + padding


def get_actual_path(path):
    try:
        _obj = Shortener.objects.filter(short_url=path).last()
        return _obj.long_url
    except:
        return None

