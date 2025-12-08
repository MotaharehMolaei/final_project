import re
from enroll_model import Enroll
from enroll_dao import EnrollDataAccess


class EnrollController:
    @staticmethod
    def is_valid_enroll(name, family, phone_number, enroll_date, level, teacher):
        if not re.match(r"^[a-zA-Z\s]{3,30}$", name):
            raise NameError("Invalid Name")

        if not re.match(r"^[a-zA-Z\s]{3,30}$", family):
            raise NameError("Invalid family name")

        if not re.match(r"^09\d{9}$", phone_number):
            raise NameError("Invalid phone number")

        if not re.match(r"^\d{4}-\d{2}-d\{2}$", enroll_date):
            raise NameError("Invalid enroll date")

        if level not in ["A1", "A2", "B1", "B2", "C1", "C2"]:
            raise NameError("Invalid level")

        if not re.match(r"^[a-zA-Z\s]{3,60}$", teacher):
            raise NameError("Invalid Teacher name")

    @staticmethod
    def save(id, name, family, phone_number, enroll_date, class_name, level, teacher):
        valid, message = EnrollController.is_valid_enroll(name, family, phone_number, enroll_date, class_name, level,teacher)
        if not valid:
            return valid, message

        try:
            enroll = Enroll(self)
            dao = EnrollDataAccess()
            dao.save(enroll)
            return True, "Enrollment saved successfully"
        except Exception as e:
            return False, f"Failed to save enrollment: {e}"

    @staticmethod
    def edit(id, name, family, phone_number, enroll_date, class_name, level, teacher):
        valid, message = EnrollController.is_valid_enroll(name, family, phone_number, enroll_date, class_name,
                                                          level, teacher)
        if not valid:
            return valid, message

        try:
            enroll = Enroll(id, name, family, phone_number, enroll_date, class_name, level, teacher)
            dao = EnrollDataAccess()
            dao.save(enroll)
            return True, "Enrollment edited successfully"
        except Exception as e:
            return False, f"Failed to edit enrollment: {e}"


    @staticmethod
    def remove(id):
        try:
            dao = EnrollDataAccess()
            dao.remove(id)
            return True, "Enrollment removed successfully"
        except Exception as e:
            return False, f"Failed to remove enrollment: {e}"


    @staticmethod
    def find_all():
        try:
            dao = EnrollDataAccess()
            return True, dao.find_all()
        except Exception as e:
            return False, f"Failed to find enrollment: {e}"



