"""
House class
"""
from .Property import Property

class House(Property):
    valid_garage = {"attached", "detached", "none"}
    valid_fenced = {"yes", "no"}