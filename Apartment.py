"""
Apartment class
"""
from .Property import Property

class Apartment(Property):
    valid_laundries = {"coin", "ensuite", "none"}
    valid_balconies = {"yes", "no", "solarium"}
    
    def __init__(self, balcony='', laundry='', **kwargs):
        # Make sure Property class is properly initialized
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry
        
    def display(self):
        # Make sure display method in Property is properly initialized
        super().display()
        print("APARTMENT DETAIS")
        print("Laundry: {}".format(self.laundry))
        print("has balcony: {}".format(self.balcony))
    
    def prompt_init():
        parent_init = Property.prompt_init()
        # Adding laundry
        laundry = ''
        while laundry.lower() not in Apartment.valid_laundries:
            laundry = input(
                "What laundry facilities does "
                "the propety have? ({})".format(
                ", ".join(Apartment.valid_laundries)))
        
        # Adding balcony
        balcony = ''
        while balcony.lower() not in Apartment.valid_balconies:
            balcony = input(
                "Does the property have a balcony? "
                "({})".format(
                ", ".join(Apartment.valid_balconies)))
        
        # Dict update method to merge new dict values
        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        
        return parent_init
    prompt_init = staticmethod(prompt_init)
