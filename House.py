"""
House class
"""
from .Property import Property

class House(Property):
    valid_garage = {"attached", "detached", "none"}
    valid_fenced = {"yes", "no"}

    def __init__(self, num_stories='', garage='', fenced='', **kwargs):
        # Make sure Property class is properly initialized
        super().__init__(**kwargs)
        self.garage = balcony
        self.fenced = laundry
        self.num_stories = num_stories
