from .Property import Property

Class Apartment(Property):
    valid_laundries = {"coin", "ensuite", "none"}
    valid_balconies = {"yes", "no", "solarium"}
    
    def __init__(self, balcony='', laundry='', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry
        
    def display(self):
        super().display()
        print("APARTMENT DETAIS")
        print("Laundry: {}".format(self.laundry))
        print("has balcony: {}".format(self.balcony))