class Student:

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def validate(self):

        if not self.name.strip():
            print("Name cannot be empty.")
            return False

        if "@" not in self.email or "." not in self.email or "gmail" not in self.email:
            print("Invalid email.")
            return False

        return True