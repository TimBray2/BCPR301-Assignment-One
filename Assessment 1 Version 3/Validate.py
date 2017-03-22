# Written By Tim Bray


class ValidateData:

    def __init__(self):
        self.validated = False
        self.validatedInput = ""

    def validate_input(self):
        print("Input has been checked")
        self.validatedCheck = True

    def get_validated_check(self):
        return self.validatedInput
