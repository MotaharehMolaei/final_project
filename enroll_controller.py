import re
from enroll_model import Enroll
from enroll_dao import EnrollDataAccess
from datetime import datetime


class EnrollController:

    @staticmethod
    def is_valid_enroll(name, family, phone_number, enroll_date, class_name, level, teacher):

        if not re.match(r"^[a-zA-Z\s]{3,30}$", name):
            return False, "Invalid Name"

        if not re.match(r"^[a-zA-Z\s]{3,30}$", family):
            return False, "Invalid Family Name"

        if not re.match(r"^09\d{9}$", phone_number):
            return False, "Invalid Phone Number"

        try:
            date_obj = datetime.strptime(enroll_date, "%Y-%m-%d")
        except ValueError:
            return False, "Invalid Enroll Date (YYYY-MM-DD)"

            # Validate date is today or in the future
        today = datetime.now().date()
        if date_obj.date() < today:
            return False, "Enroll Date cannot be in the past"

        if level not in ["A1", "A2", "B1", "B2", "C1", "C2"]:
            return False, "Invalid Level"

        if not re.match(r"^[a-zA-Z\s]{3,60}$", teacher):
            return False, "Invalid Teacher Name"

        return True, ""

    @staticmethod
    def save(id, name, family, phone_number, enroll_date, class_name, level, teacher):
        valid, message = EnrollController.is_valid_enroll(
            name, family, phone_number, enroll_date, class_name, level, teacher
        )

        if not valid:
            return False, message

        try:
            enroll = Enroll(id, name, family, phone_number, enroll_date, class_name, level, teacher)
            dao = EnrollDataAccess()
            dao.save(enroll)
            return True, "Enrollment saved successfully"
        except Exception as e:
            return False, f"Failed to save enrollment: {e}"

    @staticmethod
    def edit(id, name, family, phone_number, enroll_date, class_name, level, teacher):
        valid, message = EnrollController.is_valid_enroll(
            name, family, phone_number, enroll_date, class_name, level, teacher
        )

        if not valid:
            return False, message

        try:
            enroll = Enroll(id, name, family, phone_number, enroll_date, class_name, level, teacher)
            dao = EnrollDataAccess()
            dao.edit(enroll)
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
            enrolls = dao.find_all()
            return True, enrolls
        except Exception as e:
            return False, f"Failed to find enrollments: {e}"
