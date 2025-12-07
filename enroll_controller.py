import re
from enroll_model import Enroll

class EnrollController(Enroll):
    @staticmethod
    def is_valid_enroll(self):
        if not re.match(r"^[a-zA-Z\s]{3,30}$", self.name ):
            raise NameError("Invalid Name")

        if not re.match(r"^[a-zA-Z\s]{3,30}$", self.family):
            raise NameError("Invalid family name")

        if not re.match(r"^09\d{9}$", self.phone_number):
            raise NameError("Invalid phone number")

        if not re.match(r"^\d{4}-\d{2}-d\{2}$", self.enroll_date):
            raise NameError("Invalid enroll date")

        if self.level not in ["A1", "A2", "B1", "B2", "C1", "C2"]:
            raise NameError("Invalid level")

        if not re.match(r"^[a-zA-Z\s]{3,60}$", self.Teacher):
            raise NameError("Invalid Teacher name")