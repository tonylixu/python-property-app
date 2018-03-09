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
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        # Make sure display method in Property is properly initialized
        super().display()
        print("HOUSE DETAILS")
        print("Number of stories: {}".format(self.num_stories))
        print("Garage: {}".format(self.garage))
        print("Fenced yard: {}".format(self.fenced))
    
    