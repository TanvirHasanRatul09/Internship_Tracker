class Company:

    def __init__(self, company_name, location):
        self.company_name = company_name
        self.location = location

    def validate(self):

        if not self.company_name.strip():
            print("Company name cannot be empty.")
            return False

        if not self.location.strip():
            print("Location cannot be empty.")
            return False

        return True