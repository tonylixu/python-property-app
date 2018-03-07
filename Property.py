class Property:
    def __init__(self, square_feet='', beds='', baths='', **kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.beds = beds
        self.num_baths = baths
    
    def display(self):
        print("PROPERTY DETAILS")
        print("=" x 12)
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