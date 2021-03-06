"""
Utilities class

Contains all common functions
"""

class Utilities:
    def __init__(self):
        pass
    
    def get_valid_input(self, input_string, valid_options):
        input_string += " ({})".format(", ".join(valid_options))
        response = input(input_string)
        while response.lower() not in valid_options:
            response = input(input_string)
        return response
