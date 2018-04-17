"""
Property Class

**kwargs is for multiple inheritance chain situation

prompt_init method is made into a static method immediately after it is initially created.
Static method is associated with a class (You can treat it like class variable), rather than
a specific object instance.

Notice the super keyword won't work on static method because there is no parent object, but a
parent class.
"""
class Property:
    def __init__(self, square_feet='', beds='', baths='', **kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths
    
    def display(self):
        print("PROPERTY DETAILS")
        print("=" * 12)
        print("Square footage: {}".format(self.square_feet))
        print("Bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))
        print()
    
    def prompt_init():
        return dict(
            square_feet=input("Enter the square feet: "),
            beds=input("Enter the number of bedrooms: "),
            baths=input("Enter the number of baths: ")
        )
    
    prompt_init = staticmethod(prompt_init)
